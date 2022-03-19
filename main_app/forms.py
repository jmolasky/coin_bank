from django.forms import ModelForm
from .models import Wallet

class WalletForm(ModelForm):
    # accesses object that created ModelForm class
    class Meta:
        model = Wallet
        fields = ('name', 'location')
