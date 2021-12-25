import time

from app import *


def createLimitOrder():
    order = OrderLimit
    order.Symbol = "BTC/USDT"
    order.Side = Side.Buy
    order.Type = Type.Limit
    order.TimeInForce = TimeInForce.GTC
    order.Price = 31000.24
    order.Quantity = 0.001
    order.TPSL = False
    return order


def createMarketOrder():
    order = OrderMarket
    order.Symbol = "BTC/USDT"
    order.Side = Side.Buy
    order.Type = Type.Market
    order.Quantity = 0.001
    order.TPSL = False
    return order


def createMarketOrderWithTP():
    order = OrderMarket
    order.Symbol = "BTC/USDT"
    order.Side = Side.Buy
    order.Type = Type.Market
    order.Quantity = 0.001
    order.TPSL = True
    order.TakeProfit = 36000.00
    order.StopLoss = None
    return order


def createMarketOrderWithSL():
    order = OrderMarket
    order.Symbol = "BTC/USDT"
    order.Side = Side.Buy
    order.Type = Type.Market
    order.Quantity = 0.001
    order.TPSL = True
    order.StopLoss = 30000.12
    order.TakeProfit = None
    return order


def createMarketOrderWithTPSL():
    order = OrderMarket
    order.Symbol = "BTC/USDT"
    order.Side = Side.Buy
    order.Type = Type.Market
    order.Quantity = 0.001
    order.TPSL = True
    order.TakeProfit = 39000.12
    order.StopLoss = 31000.07
    return order


def test_createMarketOrder():
    order = createMarketOrder()
    result = CreateMarketOrder(order)
    print(result)


def test_createMarketOrderWithTP():
    order = createMarketOrderWithTP()
    result = CreateMarketOrder(order)
    print(result)


def test_createLimitOrder():
    order = createLimitOrder()
    result = CreateLimitOrder(order)
    print(result)


def test_createMultiLimitOrder():
    order = createLimitOrder()
    result = CreateMultiLimitOrder(order)
    print(result)


def test_createMarketOrderWithSL():
    order = createMarketOrderWithSL()
    result = CreateMarketOrder(order)
    print(result)


def test_createMarketOrderWithTPSL():
    order = createMarketOrderWithTPSL()
    result = CreateMarketOrder(order)
    print(result)


def test_getOpenPositions():
    result = GetOpenPositions("BTC/USDT")
    print("\n\n\n\n_____________________________________________")
    print(result)
    # print('your margin is:::', [0]['initialMargin'])
    print("_____________________________________________\n\n\n\n")


def test_getLeverageBracket():
    result = GetLeverageBracket('BTCUSDT')
    print("\n\n\n\n_____________________________________________")
    print(result)
    print("_____________________________________________\n\n\n\n")


def test_getKlines():
    result = GetKlines('BTC/USDT')
    print("\n\n\n\n_____________________________________________")
    print(time.time())
    print(result)
    print(time.time())
    print("_____________________________________________\n\n\n\n")


def test_CalcQuantity():
    amount = 15
    exchange = trader.CreateExchange(config.API_KEY_1, config.SECRET_1)
    order = createMarketOrderWithTPSL()
    print("_____________________________________________\n\n\n\n")
    print(CalcQuantity(exchange, order, amount, 10))
    print("_____________________________________________\n\n\n\n")


def test_MarketClosePosition():
    print(MarketClosePosition())


def test_SetLeverage():


# test_MarketClosePosition()
test_createMarketOrder()
# test_createMarketOrderWithTP()
# test_createLimitOrder()
# test_getOpenPositions()
# test_createMarketOrderWithSL()
# test_createMarketOrderWithTPSL()
# test_createMultiLimitOrder()
# test_getLeverageBracket()
# test_getKlines()
# test_CalcQuantity()