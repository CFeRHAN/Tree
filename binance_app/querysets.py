from binance.client import Client
from users.models import User
from .models import BinanceProfile
from django.shortcuts import render, redirect


def getDetail(request):
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

def createClient(request, profile_details):
    client = Client(api_key=profile_details['profile_api'], secret=profile_details['profile_secret'])
    print(client)
    return client

def CreateMarketOrder(request, client):
    if request.method == "POST":
        order = client.futures.create_order(
            symbol=MarketOrder.symbol,
            side=MarketOrder.side,
            type=MarketOrder.type,
            timeInForce=LimitOrder.timeInForce,
            quantity=LimitOrder.quantity,
            price=LimitOrder.price
        )
        order()
    else:
        pass