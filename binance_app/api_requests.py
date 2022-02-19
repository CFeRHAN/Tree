from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from requests.exceptions import ReadTimeout, ConnectionError
from .querysets import GetDetail



def CreateClient(request):
    """function that instansiates the Client from Binance with API and SECRET"""
    if request.method == "GET":
        profile_temp = GetDetail(request)
        clients = []
        for item in profile_temp:
            profile_api = item.api
            profile_secret = item.secret
            client = Client(profile_api, profile_secret)
            if client not in clients:
                clients.append(client)
            else:
                pass
    return 0


def CreateMarketOrder(symbol, side, order_type, timeInForce, quantity, price):
    """function that creates Market Order"""
    clients = CreateClient()
    for client in clients:
        if request.method == "POST":
            order = client.futures.create_order(symbol, side, order_type, timeInForce, quantity, price)
            if order.is_valid():
                order()
            else:
                print('there is something wrong with your order set')
        else:
            print('this function doesnt have GET method!')


def CreateLimitOrder(request):
    """function that creates Limit Order"""
    client = CreateClient()
    if request.method == "POST":
        if order.type == "BUY":
            order = client.futures.order_limit_buy(
                symbol = 'symbol',
                quantity = 'quantity',
                price = 'price'
            )
            order()
        elif order.Type == "SELL":
            order = client.futures.order_limit_sell(
                symbol = 'symbol',
                quantity = 'quantity',
                price = 'price'
            )
            order()
        else:
            print("something weird happened. your order type must be wrong!")
    else:
        print("this function doesnt have GET method!")


def CreateMultiLimitOrder(request):
    """function that creates Multi Limit Orders"""
    orders = []
    clients = CreateClient()
    for client in clients:
        if request.method == "POST":
            if order.type == "BUY":
                order = client.futures.order_limit_buy(
                    symbol='symbol',
                    quantity='quantity',
                    price='price',
                )
                if order.is_valid():
                    orders.append(order)
            elif order.type == "SELL":
                order = client.futures.order_limit_sell(
                    symbol='symbol',
                    quantity='quantity',
                    price='price',
                )
                if order.is_valid():
                    orders.append(order)
            else:
                print("something weird happened. there is a problem within your order set.")
        else:
            print("this function doesnt have GET method!")
        
        for order in orders:
            order()


def CreateMultiMarketOrder(request):
    """function that creates Multi Market Orders"""
    orders = []
    clients = CreateClient()
    for client in clients:
        if request.method == "POST":
            order = client.futures.create_order(
                symbol = 'symbol',
                side = 'side',
                type = 'type',
                timeInForce = 'timeInForce',
                quantity = 'quantity',
                price = 'price'
            )
            if order.is_valid():
                orders.append(order)
        else:
            print("this function doesnt have GET method!")
    
    for order in orders:
        order()


def GetOpenPositions(request):
    clients = CreateClient()
    for client in clients:
        if request.method == "GET":
            positions = client.futures_position_information()
            
    


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
