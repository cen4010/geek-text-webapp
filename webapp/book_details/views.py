from django.shortcuts import render
from django.db.models import Avg

from .models import Book, Review
from .forms import ReviewForm

def details(request, book_id):
    book = None

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        pass

    reviews = Book.objects.get(book=book)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.user.is_authenticated:
        try:
            review = Review.objects.get(book=book, user=request.user)
        except Review.DoesNotExist:
            review = Review(book=book, user=request.user)
    else:
        review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm(instance=review)

    return render(request, 'book_details/details.html',
            {'book': book, 'reviews': reviews, 'form': form})
