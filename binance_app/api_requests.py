from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from requests.exceptions import ReadTimeout, ConnectionError
from .models import MarketOrder, LimitOrder
from .querysets import GetDetail, CreateClient


def CreateMarketOrder(client, request):
    client = CreateClient()
    for clnt in clients:
        if request.method == "POST":
            order = clnt.futures.create_order(
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


def CreateLimitOrder(request):
    client = CreateClient()
    for clnt in clients:
        if request.method == "POST":
            order = clnt.
    pass


def CreateMultiLimitOrder(request):
    pass


def CreateMultiMarketOrder(request):
    pass


def GetOpenPositions(request):
    pass


def GetLeverageBracket(request):
    pass


def CancelOrder(request):
    pass


def CancelAllOrders(request):
    pass


def GetAllOrders(request):
    pass


def MarketClosePosition(request):
    pass


def CloseOpenPositions(request):
    pass


def CalcQuantity(request):
    pass


def SetLev(request):
    pass


def CreateBatchOrders(request):
    pass


def AdjustTPSL(request):
    pass


def AdjustMarginType(request):
    pass


