from django.forms import ModelForm

from .models import Wallet, Crypto

class WalletForm(ModelForm):
    # accesses object that created ModelForm class
    class Meta:
        model = Wallet
        fields = ('name',)

class CryptoForm(ModelForm):
    class Meta:
        model = Crypto
        fields = ('symbol',)