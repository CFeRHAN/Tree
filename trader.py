import ccxt
from Order import *
from manageParams import *
import config


def CreateExchange(apikey, secret):
    exchange = ccxt.binance({
        'apiKey': apikey,
        'secret': secret,
        'options': {
            'defaultType': 'future'
        },
    })
    exchange.verbose = True
    return exchange


def CreateOrder(exchange, order):
    if order.Type == Type.Limit:
        params = GetOrderParams(exchange, order)
        orderResult = exchange.create_order(order.Symbol, order.Type.value, order.Side.value, order.Quantity, order.Price, params)
        return orderResult
    elif order.Type == Type.Market:
        params = GetOrderParams(exchange, order)
        orderResult = exchange.create_order(order.Symbol, order.Type, order.Side, order.Amount, params)
        return orderResult
    elif order.Type == Type.TakeProfit:
        params = GetOrderParams(exchange, order)
        orderResult = exchange.create_order(order.Symbol, order.Type, order.Side, order.Amount, order.Price, params)
        return orderResult
    elif order.Type == Type.TakeProfitMarket:
        params = GetOrderParams(exchange, order)
        orderResult = exchange.create_order(order.Symbol, order.Type, order.Side, order.Amount, params)
        return orderResult


def CancelOrder(exchange, symbol, orderId):
    orderResult = exchange.cancelOrder(orderId, symbol)
    return orderResult
