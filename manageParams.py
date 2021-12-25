import ccxt
from Order import *


def SetSymbolLeverage(exchange, symbol, lev):
    market = exchange.market(symbol)
    response = exchange.fapiPrivate_post_leverage({
        'symbol': market['id'],
        'leverage': lev,
    })
    return response


def GetTPParams(stopPrices):
    params = {
        # 'stopPrice': exchange.exchange.price_to_precision(symbol, stopPrices, ),
        'stopPrice': stopPrices,
        # 'price': float(36000.00),
    }
    return params


def GetSLParams(stopLoss):
    params = {
        # 'type': 'STOP_MARKET',
        'stopPrice': stopLoss,
    }
    return params


def GetOrderParams(exchange, order):
    if order.Type == Type.TakeProfit:
        params = {
            'type': 'takeProfit',
            'price': order.Price
        }
        return params
    elif order.Type == Type.TakeProfitMarket:
        params = {
            'type': 'takeProfitMarket'
        }
        return params
    elif order.Type == Type.Stop:
        params = {
            'type': 'stopLoss',
        }
        return params
    elif order.Type == Type.StopMarket:
        params = {
            'type': 'stopMarket',
            'stopPrice': order.StopPrice
        }
        return params
    elif order.Type == Type.LimitMaker:
        params = {
            'type': 'limitMaker',
            'quantity': order.Quantity,
            'price': order.Price
        }
        return params
