from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BinanceProfile
from django.contrib import messages
from .forms import BinanceProfileForm
from users.forms import UserUpdateForm
from django.http import HttpResponse


@login_required
def binance_profile(request):
    """shows a binance profile"""
    if request.method == 'GET':
        profile_temp = BinanceProfile.objects.filter(user=request.user).first()
        profile_api = profile_temp.api
        profile_secret = profile_temp.secret
        profile_details = {
        'profile_api': profile_api,
        'profile_secret': profile_secret,
        }
        """a test on profile"""
        print("this is profile: ", profile_details)
    else:
        pass
    return render(request, 'binance_profile.html', profile_details)