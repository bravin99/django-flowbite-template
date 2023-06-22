from django.shortcuts import render
from main_app.forms import ContactForm
from django.contrib import messages


def landing_page(request):
    messages.info(request, "Hello")
    messages.success(request, "Hello 2")
    messages.error(request, "Hello 3")
    messages.warning(request, "Nice to meet yah")
    return render(request, 'main_app/landing.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent")
        else:
            messages.error(request, "Error in submitted message")
    else:
        form = ContactForm()

    return render(request, 'main_app/contact.html', context = {
        'form': form,
    })

