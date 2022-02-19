from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import FollowersCount
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from binance_app.forms import BinanceProfileForm
from binance_app.models import BinanceProfile
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Congrats {username}! Your account is up and you can login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        b_form = BinanceProfileForm(request.POST)
        #print(request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            b_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        b_form = BinanceProfileForm(instance=request.user.binanceprofile)
        #print(request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'b_form': b_form
    }
    return render(request, 'users/profile.html', context)


def followers_count(request):
    current_user = request.Get.get('user')
    logged_in_user = request.user.username
    followers_count = len(FollowersCount.objects.filter(user=current_user))
    followers_temp = FollowersCount.objects.filter(user=current_user)
    user_followers = []
    for i in followers_temp:
        followers_temp = i.follower
        user_followers.append(followers_temp)

    if logged_in_user in user_followers:
        follow_button_value = 'unfollow'
    else:
        follow_button_value = 'follow'

    return render(request, 'main.html', {'current_user':current_user,
                                         'followers_count': followers_count,
                                         'following_count': followers_count,
                                         'follow_button_value': follow_button_value})

def follow(request):
    if request.method == 'POST':
        value = request.POST['value']
        user = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            followers_cnt = FollowersCount.objects.create(follower=follower, user=user)
            followers_cnt.save()
        elif value == 'unfollow':
            followers_cnt = FollowersCount.objects.get(follower=follower, user=user)
            followers_cnt.delete()
        return redirect('/?user'+ user)