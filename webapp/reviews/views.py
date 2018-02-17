from django.shortcuts import render

from book_details.models import Book
from reviews.models import Review

def reviews(request, book_id):
    book = None
    reviews = None

    try:
        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book=book)
    except Book.DoesNotExist:
        pass

    return render(request, 'reviews/reviews.html', {'book': book, 'reviews': reviews})
