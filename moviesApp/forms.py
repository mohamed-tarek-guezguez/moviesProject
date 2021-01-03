from django.forms import ModelForm
from django import forms
from .models import Contact

class contactForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
