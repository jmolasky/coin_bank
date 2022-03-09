from django.contrib import admin
from .models import Crypto, Wallet

# Register your models here.

admin.site.register(Crypto)
admin.site.register(Wallet)
