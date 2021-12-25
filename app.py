import csv

import ccxt

import Order
import config
import trader
from Order import *
from manageParams import *


def CreateMarketOrder(order):
    exchange = trader.CreateExchange(config.API_KEY_2, config.SECRET_2)
    if order.Type == Type.Market:
        if order.Side == Side.Buy:
            result = exchange.create_order(order.Symbol, 'MARKET', 'buy', float(order.Quantity))
        elif order.Side ==Side.Sell:
            result = exchange.create_order(order.Symbol, 'MARKET', 'sell', float(order.Quantity))
        # if order.Side == Side.Buy:
        #     result = exchange.create_order(order.Symbol, 'MARKET', order.Side,
        #                                    float(order.Quantity))
        #     # return result
        # elif order.Side == Side.Sell:
        #     result = exchange.create_market_sell_order(order.Symbol, float(order.Quantity))
        #     # return result
        if order.TPSL is True:
            if order.TakeProfit:
                params = GetTPParams(float(order.TakeProfit))
                result = exchange.create_order(order.Symbol, 'TAKE_PROFIT_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.TakeProfit), params)
            if order.StopLoss:
                params = GetSLParams(float(order.StopLoss))
                result = exchange.create_order(order.Symbol, 'STOP_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.StopLoss), params)
    return result


def CreateLimitOrder(order):
    exchange = trader.CreateExchange(config.API_KEY_2, config.SECRET_2)
    if order.Type == Type.Limit:
        result = exchange.create_order(order.Symbol, 'LIMIT', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.Price))
        if order.TPSL is True:
            if order.TakeProfit:
                params = GetTPParams(float(order.TakeProfit))
                result = exchange.create_order(order.Symbol, 'TAKE_PROFIT_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.TakeProfit), params)
            if order.StopLoss:
                params = GetSLParams(float(order.StopLoss))
                result = exchange.create_order(order.Symbol, 'STOP_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.StopLoss), params)


def CreateMultiLimitOrder(order):
    finalResult = []
    with open("Keys.csv", "r") as f:
        contents = csv.reader(f)
        for c in contents:
            exchange = trader.CreateExchange(c[1], c[2])
            if order.Type == Type.Limit:
                result = exchange.create_order(order.Symbol, 'LIMIT', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.Price))
                finalResult.append(result)
                if order.TPSL is True:
                    if order.TakeProfit:
                        params = GetTPParams(float(order.TakeProfit))
                        result = exchange.create_order(order.Symbol, 'TAKE_PROFIT_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.TakeProfit), params)
                        finalResult.append(result)
                    if order.StopLoss:
                        params = GetSLParams(float(order.StopLoss))
                        result = exchange.create_order(order.Symbol, 'STOP_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.StopLoss), params)
                        finalResult.append(result)
    return finalResult


def CreateMultiMarketOrder(order):
    finalResult = []
    with open("Keys.csv", "r") as f:
        contents = csv.reader(f)
        for c in contents:
            exchange = trader.CreateExchange(c[1], c[2])
            if order.Type == Type.MARKET:
                result = exchange.create_order(order.Symbol, 'MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity))
                finalResult.append(result)
                if order.TPSL is True:
                    if order.TakeProfit:
                        params = GetTPParams(float(order.TakeProfit))
                        result = exchange.create_order(order.Symbol, 'TAKE_PROFIT_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.TakeProfit), params)
                        finalResult.append(result)
                    if order.StopLoss:
                        params = GetSLParams(float(order.StopLoss))
                        result = exchange.create_order(order.Symbol, 'STOP_MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity), float(order.StopLoss), params)
                        finalResult.append(result)
    return finalResult


def GetOpenPositions(symbol):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    result = exchange.fetch_positions(symbol)
    return result


def GetLeverageBracket(symbol):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    result = exchange.load_leverage_brackets(False, {'symbol': symbol})
    # result = exchange.load_leverage_brackets()
    return result


def CancelOrder(orderId, symbol):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    result = trader.CancelOrder(exchange, symbol, orderId)
    return result


def GetAllOrders(symbol):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    result = exchange.fetchOrders()
    return result


def CancelAllOrders(symbol):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    resault = exchange.cancel_all_orders(symbol)
    return resault


def MarketClosePosition():
    # exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    order = OrderMarket
    _symbol = order.Symbol = 'BTC/USDT'
    temp = GetOpenPositions(_symbol)
    order.Type = Type.Market
    if temp[0]["side"] == 'long':
        order.Quantity = float(temp[0]['info']['positionAmt'])
        order.Side = Side.Sell
    elif temp[0]["side"] == 'short':
        order.Quantity = float(temp[0]['info']['positionAmt']) * (-1)
        order.Side = Side.Buy
    else:
        pass

    # create market order to close th given position!
    # result = exchange.x()

    CreateMarketOrder(order)


def CloseOpenPositions(symbol):
    finalResult = []
    with open("Keys.csv", "r") as f:
        contents = csv.reader(f)
        for c in contents:
            exchange = trader.CreateExchange(c[1], c[2])
            position = exchange.fetch_positions(symbol)
            order = OrderMarket
            order.Symbol = symbol
            order.Type = Type.Market
            order.Quantity = float(position[0]['info']['positionAmt'])
            order.Side = Side.Sell if position[0]['side'] == 'long' else Side.Buy
            order.TPSL = False
            order.TakeProfit = None
            order.StopLoss = None
            result = exchange.create_order(order.Symbol, 'MARKET', 'buy' if order.Side == Side.Buy else 'sell', float(order.Quantity))
            finalResult.append(result)
    return result


# M-def calc quntity
# fetching margin usdt balance and calculate it to precision quantity
def CalcQuantity(exchange, order, amount, lev):
    balance = exchange.fetchBalance()
    postionAmount = ((float(balance['info']['totalMarginBalance'])) * float(amount)) / 100  # calc percentage of wallet base on amount(amount should be percentage like 15%)
    symbolPrice = exchange.fetchTickers([order.Symbol])[order.Symbol]['last']
    # pricePrecision = exchange.markets['ETH/USDT']['info']['pricePrecision']
    pricePrecision = exchange.markets[order.Symbol]['precision']['amount']
    order_amount = (postionAmount / float(symbolPrice)) * lev
    precise_order_amount = "{:0.0{}f}".format(order_amount, pricePrecision)  # string of precise order amount that can be used when creating order
    print(order_amount, "\n", precise_order_amount)
    return precise_order_amount


def SetLev(symbol, leverage):
    finalResult = []
    with open("Keys.csv", "r") as f:
        contents = csv.reader(f)
        for c in contents:
            exchange = trader.CreateExchange(c[1], c[2])
            result = exchange.set_leverage(symbol, leverage)
            finalResult.append(result)
    return finalResult


def SetLeverage(symbol, leverage):
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    with open("C:/Users/farideh/PycharmProjects/MarioTrader-CCXT/Keys.csv", "r") as f:
        # with open("Keys.csv", "r") as f:
        contents = csv.reader(f)
        for c in contents:
            # exchange = trader.CreateExchange(c[1], c[2])
            exchange = trader.CreateExchange(c[1], c[2])
    symbol = 'BTCUSDT'  # temp symbol
    exchange.set_leverage(symbol, leverage)
    # markets = exchange.load_markets()
    # symbol = 'BTC/USDT'
    # market = exchange.market(symbol)
    #
    # response = exchange.fapiPrivatePostLeverage({
    #     'symbol': market['id'],  # market id
    #     'leverage': 1})
    # # return response
