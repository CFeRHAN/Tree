from django import forms
from .models import BinanceProfile


class BinanceProfileForm(forms.ModelForm):
    class Meta:
        model = BinanceProfile
        fields = ['api', 'secret']
