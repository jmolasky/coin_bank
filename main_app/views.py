from django.shortcuts import render, redirect
from .models import Wallet, CryptoCurrency, Amount
from .forms import WalletForm
from decouple import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Create your views here.

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
api_key = config('api_key')

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

def home(request):
    return render(request, 'home.html')

def wallets_index(request):
    # get all wallets
    wallets = Wallet.objects.all()
    symbols_arr = []
    wallets_arr = []
    for wallet in wallets:
        coins_arr = []
        wallet_coins = Amount.objects.filter(wallet=wallet.id)
        for coin in wallet_coins:
            if (coin.crypto.symbol not in symbols_arr):
                symbols_arr.append(coin.crypto.symbol)
            coin_object = {
                'symbol': coin.crypto.symbol,
                'amount': coin.amount,
            }
            coins_arr.append(coin_object)
        wallet_obj = {
            'id': wallet.id,
            'name': wallet.name,
            'coins': coins_arr,
        }
        # add coins_not_in_wallet to each wallet
        wallet_obj['coins_not_in_wallet'] =  CryptoCurrency.objects.exclude(id__in=wallet_coins.values_list('crypto'))
        wallets_arr.append(wallet_obj)
    # get all symbols in all wallets
    symbols = ','.join(symbols_arr)
    parameters = {
        'symbol': symbols
    }
    session = Session()
    session.headers.update(headers)
    try:
        # api call for all coins in all wallets
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        data = data['data']
        coins = []
        for symbol in symbols_arr:
            coin_obj = data[symbol][0]
            obj = {
                'symbol': symbol,
                'name': coin_obj['name'],
                'last_updated': coin_obj['last_updated'],
                'quote': coin_obj['quote']['USD'],
            }
            coins.append(obj)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    for wallet in wallets_arr:
        for coin in wallet['coins']:
            for obj in coins:
                if obj['symbol'] == coin['symbol']:
                    coin['price'] = obj['quote']['price']
                    coin['name'] = obj['name']
    print(f"wallets array: {wallets_arr}")
    wallet_form = WalletForm()
    return render(request, 'dashboard.html', {
        'wallets': wallets_arr,
        'wallet_form': wallet_form,
    })

def add_wallet(request):
    form = WalletForm(request.POST)
    if form.is_valid():
        new_wallet = form.save(commit=False)
        # this is where you would attach the user id with request.user
        new_wallet.save()
    return redirect('dashboard')

def wallets_detail(request, wallet_id):
    wallet = Wallet.objects.get(id=wallet_id)
    wallet_coins = Amount.objects.filter(wallet=wallet.id)
    coins_not_in_wallet = CryptoCurrency.objects.exclude(id__in=wallet_coins.values_list('crypto'))
    wallet_obj = {
        'id': wallet.id,
        'name': wallet.name,
        'coins': wallet_coins,
    }
    return render(request, 'wallets/detail.html', { 
        'wallet': wallet_obj, 
        'avail_coins': coins_not_in_wallet 
    })

