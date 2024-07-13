from django.urls import path
from .views import login_view, regester_view, logout_view, account, about, buy, need

urlpatterns = [
    path('login/', login_view, name='login'),
    path('regester/', regester_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('account/', account, name='account'),
    path('about/', about, name='about'),
    path('buy/', buy, name='buy_book'),
    path('need/', need, name='need_book')
]
