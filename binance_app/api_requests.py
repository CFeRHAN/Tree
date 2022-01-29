from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from requests.exceptions import ReadTimeout, ConnectionError
from .models import MarketOrder, LimitOrder
from .querysets import clients



def GetInfo(client):
    info = client.futures_exchange_info()
    return info


def Loop():
    for i in clients:
        clnt = i
        return clnt


def CreateMarketOrder(client, request):
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

