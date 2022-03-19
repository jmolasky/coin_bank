from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('wallets/', views.wallets_index, name='dashboard'),
    # this is the path for the detail page, but the detail page is also the edit page for 
    # the wallets
    path('wallets/<int:wallet_id>', views.wallets_detail, name='detail'),
    path('wallets/create', views.add_wallet, name='add_wallet'),
    path('crypto/', views.CryptoList.as_view(), name='crypto_list'),
    path('crypto/add_crypto', views.add_crypto, name='add_crypto'),
]