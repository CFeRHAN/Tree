from binance.client import Client
from users.models import User
from .models import BinanceProfile as BP


"""create client"""
# api = BP.objects.get("api")
# secret = BP.objects.get("secret")

# print(api, secret)
# clients = []
# for i, j in api, secret:
#     client = Client(api_key=api, secret_key=secret)
#     client.append(Clients)

bp = BinanceProfile.objects.all()

print(bp)
