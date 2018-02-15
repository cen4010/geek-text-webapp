from django.shortcuts import render

from .models import Book

def details(request, book_id):
    book = None

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        pass

    return render(request, 'book_details/details.html', { 'book': book })
