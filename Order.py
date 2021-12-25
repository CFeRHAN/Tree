import enum

from binance import enums as EnumsB
import pandas as pd
from decimal import Decimal


class Side(enum.Enum):
    Buy = EnumsB.SIDE_BUY
    Sell = EnumsB.SIDE_SELL


class Type(enum.Enum):
    Limit = EnumsB.FUTURE_ORDER_TYPE_LIMIT
    Market = EnumsB.FUTURE_ORDER_TYPE_MARKET
    Stop = EnumsB.FUTURE_ORDER_TYPE_STOP
    StopMarket = EnumsB.FUTURE_ORDER_TYPE_STOP_MARKET
    TakeProfit = EnumsB.FUTURE_ORDER_TYPE_TAKE_PROFIT
    TakeProfitMarket = EnumsB.FUTURE_ORDER_TYPE_TAKE_PROFIT_MARKET
    LimitMaker = EnumsB.FUTURE_ORDER_TYPE_LIMIT_MAKER


class Order:
    Symbol = ''
    Side = Side
    Type = Type
    Timestamp = pd.Timestamp
    TPSL = False
    TakeProfit = Decimal
    StopLoss = Decimal


class TimeInForce(enum.Enum):
    GTC = EnumsB.TIME_IN_FORCE_GTC
    FOK = EnumsB.TIME_IN_FORCE_FOK
    GTX = EnumsB.TIME_IN_FORCE_GTX
    IOC = EnumsB.TIME_IN_FORCE_IOC


class OrderMarket(Order):
    Quantity = Decimal


class OrderLimit(OrderMarket):
    TimeInForce = TimeInForce
    Price = Decimal


class OrderStopMarket(OrderMarket):
    StopPrice = Decimal
    ClosePosition = bool
    PriceProtect = bool


class OrderTakeProfit(OrderStopMarket):
    Price = Decimal


class OrderTakeProfitMarket(OrderStopMarket):
    ClosePosition = bool
    PriceProtect = bool


class OrderTrailingStopMarket(Order):
    CallBackRate = Decimal
    ActivationPrice = Decimal
