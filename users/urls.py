from django.urls import path
from .views import login_view, regester_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('regester/', regester_view, name='register'),
    path('logout/', logout_view, name='logout')
]
