from django.core.mail import EmailMessage
from django.template.loader import get_template
from smtplib import SMTPException, SMTPAuthenticationError, SMTPServerDisconnected
from socket import error as socketerror
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib import messages


def send_newsletter(request, receivers, subject, message_body):
    context = {
        'subject': subject,
        'message_body': message_body
    }
    message = get_template('emails/newsletter.html').render(context)
    try:
        msg = EmailMessage(subject, message, DEFAULT_FROM_EMAIL, receivers)
        msg.content_subtype = "html"
        msg.send()
        messages.success(request, "Newsletter has been sent")
    except (SMTPException, SMTPAuthenticationError, SMTPServerDisconnected, socketerror) as exc:
        messages.error(request, "Failed to send newsletter")

