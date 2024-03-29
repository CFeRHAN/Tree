from django.db import models
from users.models import Profile
import pandas as pd
from django.contrib.auth.models import User

SIDE_CHOICES = [('BUY', 'BUY'),
                ('SELL', 'SELL'),
                ]


TYPE_CHOICES = [('LIMIT', 'LIMIT'),
                ('MARKET', 'MARKET'),
                ('STOP', 'STOP'),
                ('TAKE_PROFIT', 'TAKE_PROFIT'),
                ('STOP_MARKET', 'STOP_MARKET'),
                ('TAKE_PROFIT_MARKET', 'TAKE_PROFIT_MARKET'),
                ('TRAILING_STOP_MARKET', 'TRAILING_STOP_MARKET'),
                ]

TIME_CHOICES = [('GTC', 'GTC'),     # Good till cancelled
                ('IOC', 'IOC'),     # Immediate or cancel
                ('FOK', 'FOK'),     # Fill or kill
                ('GTX', 'GTX'),     # Post only order
                ]


class BinanceProfile(models.Model):
    """Model for binance profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    api = models.CharField(max_length=65)
    secret = models.CharField(max_length=65)
    positions = models.JSONField(null=True, blank=True)
    long_positions = models.IntegerField(default=0)
    short_positions = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user} binance profile'



class Currency(models.Model):
    """Model for crypto currencies with symbol and amount"""
    name = models.ForeignKey(BinanceProfile, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    amount = models.FloatField(db_index=True, default=0)

    def __str__(self):
        return f'{self.symbol}, {self.amount} - {self.name}'


class Order(models.Model):
    symbol = models.CharField(max_length=15, blank=False)
    side = models.CharField(choices=SIDE_CHOICES, max_length=4, blank=False)
    type_n = models.CharField(choices=TYPE_CHOICES, max_length=25, blank=False)
    timeStamp = pd.Timestamp

    def __str__(self):
        return f"{self.symbol}, {self.side}"


class MarketOrder(Order):
    quantity = models.FloatField(blank=False)


class LimitOrder(MarketOrder):
    timeInForce = models.CharField(choices=TIME_CHOICES, max_length=4, blank=False)
    price = models.FloatField(blank=False)


class STPMarket(Order):
    stopPrice = models.FloatField(blank=False)


class STPLimit(MarketOrder):
    stopPrice = models.FloatField(blank=False)


class TrailingStopMarket(Order):
    callbackRate = models.FloatField(blank=False)



