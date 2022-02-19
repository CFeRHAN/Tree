from django import forms
from django.forms import ModelForm
from .models import BinanceProfile


class BinanceProfileForm(ModelForm):
    class Meta:
        model = BinanceProfile
        fields = ['api', 'secret']