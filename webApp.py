import flask
from flask import Flask, redirect, request, render_template, jsonify
from Order import *
import pandas as pd
import app as ap
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/market/createLimitOrder/<symbol>", methods=['POST'])
def CreateLimitOrder(symbol):
    data = json.loads(request.data.decode("utf-8"))
    order = OrderLimit
    order.Symbol = data.get('symbol')
    order.Side = Side.Buy if data.get('side') == 'buy' else Side.Sell
    order.Type = Type.Limit
    order.TimeInForce = TimeInForce.GTC
    order.Price = data.get('price')
    order.Timestamp = pd.Timestamp.now()
    if data.get('TPSL') is True:
        order.TPSL = data.get('TPSL')
        if data.get('takeProfit'):
            order.TakeProfit = data.get('takeProfit')
        if data.get('stopLoss'):
            order.StopLoss = data.get('stopLoss')
    result = ap.CreateMultiLimitOrder(order)
    return render_template("index.html")


@app.route("/market/createMarketOrder/<symbol>", methods=['POST'])
def CreateMarketOrder(symbol):
    data = json.loads(request.data.decode("utf-8"))
    order = OrderMarket
    order.Symbol = data.get('symbol').replace('-', '/')
    order.Side = Side.Buy if data.get('side') == 'buy' else Side.Sell
    order.Type = Type.Market
    order.Quantity = Decimal(data.get('amount'))
    if data.get('TPSL') is True:
        order.TPSL = data.get('TPSL')
        if data.get('takeProfit'):
            order.TakeProfit = Decimal(data.get('takeProfit'))
        if data.get('stopLoss'):
            order.StopLoss = Decimal(data.get('stopLoss'))
    # result = ap.CreateMultiMarketOrder(order)
    result = ap.CreateMarketOrder(order)
    print(result)
    return render_template("index.html", response={"status": "OK"})


@app.route("/market/openPositions/<symbol>", methods=['GET'])
def GetOpenPositions(symbol):
    result = jsonify(ap.GetOpenPositions(symbol))
    return render_template("index.html", positions=result)


@app.route("/market/openOrders/<symbol>", methods=['GET'])
def GetOrders(symbol):
    result = ap.GetAllOrders(symbol)
    return render_template("index.html", orders=result)


@app.route("/market/cancelAllOrders/<symbol>", methods=['GET'])
def CancelAllOrders(symbol):
    result = ap.CancelAllOrders(symbol)


@app.route("/market/cancelOrder/<symbol>/<orderId>", methods=['GET'])
def CancelOrders(symbol, orderId):
    result = ap.CancelOrder(orderId, symbol)
    json = {}
    flask.flash(result, {'json': json})


@app.route("/market/marketOpenPosition/<symbol>", methods=['GET'])
def MarketOpenPosition(symbol):
    result = ap.CloseOpenPositions(symbol.replace('-', '/'))
    return 0


@app.route("/market/setLeverage/<symbol>/<lev>", methods=['GET'])
def SetLeverage(symbol, lev):
    result = ap.SetLeverage(symbol.replace('-', '/'), lev)
    return result


if __name__ == '__main__':
    app.run(debug=True)

