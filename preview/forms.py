# forms.py
from django import forms
from .models import NewsletterSubscriber

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
