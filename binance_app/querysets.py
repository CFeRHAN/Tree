from binance.client import Client
from .models import BinanceProfile


def CreateClient():
    queryset = BinanceProfile.objects.all()
    for i in queryset:
        api = queryset['api']
        secret = queryset['secret']
        client = Client(api, secret)
        client.futures_create_order()
    return client