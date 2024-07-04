from django.shortcuts import render
from .models import Book, Author


def home(request):
    return render(request, 'home.html')


def book(request):
    book = Book.objects.all()
    context = {"all_book": book}
    return render(request, 'book.html', context=context)


def author(request):
    author = Author.objects.all()
    context = {"all_author": author}
    return render(request, 'author.html', context=context)
