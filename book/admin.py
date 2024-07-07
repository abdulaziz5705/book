from django.contrib import admin
from .models import Author, Book

# admin.site.register(Book)
# admin.site.register(Author)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'yili', 'tili']
    list_display_links = ['title','author']
    search_fields = ['title']
