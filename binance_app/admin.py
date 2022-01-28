from django.contrib import admin
from .models import BinanceProfile, Currency, Order, MarketOrder, LimitOrder, STPMarket, STPLimit, TrailingStopMarket


admin.site.register(BinanceProfile)
admin.site.register(Currency)
admin.site.register(Order)
admin.site.register(MarketOrder)
admin.site.register(LimitOrder)
admin.site.register(STPMarket)
admin.site.register(STPLimit)
admin.site.register(TrailingStopMarket)

