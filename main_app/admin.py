from django.contrib import admin
from .models import Crypto, Wallet, Amount

# Register your models here.

admin.site.register(Crypto)
admin.site.register(Wallet)
admin.site.register(Amount)
