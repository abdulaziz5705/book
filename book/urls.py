from django.urls import path
from .views import home, book, author

urlpatterns = [
    path('', home, name='home'),
    path('book/', book, name='book'),
    path('author/', author, name='author')
]


