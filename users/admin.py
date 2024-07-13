from django.contrib import admin
from .models import UserBook, NeedBook


@admin.register(NeedBook)
class NeedBook(admin.ModelAdmin):
    list_display = ['id', 'book', 'user']
    list_display_links = ['user']
    search_fields = ['book']


@admin.register(UserBook)
class UserBook(admin.ModelAdmin):
    list_display = ['id', 'book', 'user']


