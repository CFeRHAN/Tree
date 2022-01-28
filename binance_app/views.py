from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BinanceProfile
from .forms import BinanceProfileForm
from users.forms import UserUpdateForm
from django.contrib.auth.decorators import login_required


@login_required
def binance_profile(request):
    """creates a binance profile"""
    if request.method == 'POST':
        b_form = BinanceProfileForm(request.POST, instance=request.user)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f'Your Binance Account Created!')
            return redirect('binance_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        b_form = BinanceProfileForm(instance=request.user)
    context = {
        'u_form': u_form,
        'b_form': b_form
    }
    return render(request, 'binance_profile.html', context)