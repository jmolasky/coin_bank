from django.contrib import admin
from .models import CryptoCurrency, Wallet, Amount
# Register your models here.

admin.site.register(CryptoCurrency)
admin.site.register(Wallet)
admin.site.register(Amount)