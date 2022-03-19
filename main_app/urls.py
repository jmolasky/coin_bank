from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wallets/', views.wallets_index, name='dashboard'),
    path('wallets/<int:wallet_id>', views.wallets_detail, name='detail'),
    path('wallets/create', views.add_wallet, name='add_wallet'),
]