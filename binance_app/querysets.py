from django.contrib.auth.models import User
from .models import BinanceProfile
from django.shortcuts import render, redirect

def GetDetail(request):
    """return profile API/SECRET"""
    profile_temp = BinanceProfile.objects.all()
    print(f'this is profile_temp::: ',profile_temp)
    return profile_temp


