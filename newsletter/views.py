from django.shortcuts import render, HttpResponseRedirect, redirect
from newsletter.models import Subscriber, Newsletter
from django.contrib import messages
import uuid
from smtplib import SMTPException, SMTPAuthenticationError, SMTPServerDisconnected
from socket import error as SocketError
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['full_name']

        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered")
        else:
            confirmation_id = uuid.uuid4()
            Subscriber.objects.create(email=email, name=name,
                                      confirmation_id=confirmation_id)
            messages.success(request, "Your subscription was successful, "
                                      "check your inbox for confirmation link")
            try:
                site = get_current_site(request)
                email_subject = 'Email confirmation for our newsletter'
                message = render_to_string('emails/confirm_newsletter_email.html', {
                    'domain': site.domain,
                    'name': name,
                    'confirm_code': confirmation_id
                })
                email_message = EmailMessage(email_subject, message, to=[email])
                email_message.send()
            except (SMTPException, SMTPAuthenticationError, SMTPServerDisconnected, SocketError) as exc:
                messages.error(request, "Error sending email")
                # TODO: log error
                print(exc)

    return redirect(request.META.get('HTTP_REFERER'))


def unsubscribe(request):
    email = request.GET['email']

    try:
        subscriber = Subscriber.objects.get(email=email)
        subscriber.receive_emails = False
        subscriber.save()
        messages.success(request, "unsubscribe was successful")
    except Subscriber.DoesNotExist:
        messages.error(request, 'You are not subscribed to our mailing list')
    except Exception as exc:
        messages.error(request, 'Operation failed, please try again')

    return redirect('landing')


def confirmation(request, confirmation_id):
    try:
        subscriber = Subscriber.objects.get(confirmation_id=confirmation_id)
        subscriber.confirmed = True
        subscriber.save()
        messages.success(request, 'Email address confirmed')
        return redirect('landing')
    except Subscriber.DoesNotExist:
        messages.error(request, 'You must register your email before confirmation')

    return render(request, 'confirm_email.html')
