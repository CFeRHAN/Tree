from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BinanceProfile
from .forms import BinanceProfileForm
from users.forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def binance_profile(request):
    """creates a binance profile"""
    if request.method == 'GET':
        profile_temp = BinanceProfile.objects.all().filter(user=request.user)
        profile = BinanceProfile.objects.filter(api__in=profile_temp)
        profiles = []
        for i in profile:
            profiles.append(i)

        
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    return render(request, 'binance_profile.html', {'profiles':profiles})