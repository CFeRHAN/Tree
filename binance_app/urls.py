from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import binance_profile


urlpatterns = [
    path('binance_profile/', binance_profile, name='binance_profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)