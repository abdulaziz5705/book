from django.shortcuts import render
from .models import Book, Author


def home(request):
    return render(request, 'home.html')


def book(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        return render(request, 'book.html', {'books': books, 'values': search,})
    book = Book.objects.all()
    return render(request, 'book.html', {'book': book})


def author(request):
    author = Author.objects.all()
    context = {"all_author": author}
    return render(request, 'author.html', context=context)
