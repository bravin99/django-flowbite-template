from django.shortcuts import render, HttpResponseRedirect, redirect
from newsletter.models import Subscriber, Newsletter
from django.contrib import messages
import uuid


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
            messages.success(request, "Your subscription was successful")

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
