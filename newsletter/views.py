from django.shortcuts import render, HttpResponseRedirect, redirect
from newsletter.models import Subscriber, Newsletter
from django.contrib import messages


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['full_name']

        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered")
        else:
            Subscriber.objects.create(email=email, name=name)
            messages.success(request, "Your subscription was successful")

    return redirect(request.META.get('HTTP_REFERER'))
