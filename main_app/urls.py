from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('wallets/', views.wallets, name='wallets'),
    path('wallets/<int:wallet_id>', views.wallets_detail, name='detail'),

]


