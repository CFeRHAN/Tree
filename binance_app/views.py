from django.shortcuts import render, redirect
from .api_requests import CreateMarketOrder
from rest_framework.views import APIViews
from rest_framework.response import Response


class MarketOrder(APIViews):
    def get(self, request):
        symbol = request.GET.get('symbol')
        side = request.GET.get('side')
        order_type = request.GET.get('type')
        timeINForce = request.GET.get('timeINForce')
        quantity = request.GET.get('quantity')
        temp = CreateMarketOrder(symbol, side, order_type, timeINForce, quantity)
        return Response(temp, status=200)
