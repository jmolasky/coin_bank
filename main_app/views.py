from .models import Wallet, Crypto, Amount
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid signup - please try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error': error_message,
    }
    return render(request, 'registration/signup.html', context)

def wallets_index(request):
    wallets = Wallet.objects.all()
    return render(request, 'wallets/index.html', {'wallets': wallets})

def wallets_detail(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id)
    # query database for a specific wallet's coins
    wallet_coins = Amount.objects.filter(wallet=wallet_id)
    # TODO: use the API to pull additional data about each currency to display - will need to do some
    # math etc. to get this to work but it should be doable
   
    coins_not_in_wallet = Crypto.objects.exclude(id__in=wallet_coins.values_list('crypto'))

    return render(request, 'wallets/detail.html', {
        'wallet': wallet,
        'avail_coins': coins_not_in_wallet,
        'coins': wallet_coins,
    })