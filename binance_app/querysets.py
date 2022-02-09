from binance.client import Client
from users.models import User
from .models import BinanceProfile
from django.shortcuts import render, redirect




def GetDetail(request):
    """gives profile API/Secret"""
    profile_temp = BinanceProfile.objects.filter(user=request.user).first()
    profile_api = profile_temp.api
    profile_secret = profile_temp.secret
    profile_details = {
        'profile_api': profile_api,
        'profile_secret': profile_secret,
    }
    print(profile_details)
    return profile_details

def CreateClient(request, profile_details):
    """function that instansiates the Client from Binance with Api and Secret"""
    clients = []
    for profile_api, profile_secret in profile_details:
        client = Client(api_key=profile_details['profile_api'], secret=profile_details['profile_secret'])
        if client not in clients:
            clients.append(client)
        else:
            pass 
    print(clients)
    return clients
