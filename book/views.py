from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Book, Author


def home(request):
    return render(request, 'home.html')

@login_required
def book(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        return render(request, 'book.html', {'books': books, 'values': search,})
    book = Book.objects.all()
    return render(request, 'book.html', {'book': book})

@login_required
def author(request):
    author = Author.objects.all()
    context = {"all_author": author}
    return render(request, 'author.html', context=context)


def book_detail(request, id):
    book_detail_1 = Book.objects.get(id=id)
    if book_detail_1:
        return render(request, 'book_detail.html', {'book': book})
    else:
        return render(request, 'book_detail.html', {'book': book})
