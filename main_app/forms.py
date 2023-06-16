from django import forms
from main_app.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ['full_name', 'email', 'phone', 'message', 'call_back']

