from django.shortcuts import render
from django.db.models import Avg

from book_details.models import Book
from reviews.models import Review
from reviews.forms import ReviewForm

def reviews(request, book_id):
    book = None
    reviews = None
    average_rating = None

    try:
        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book=book)
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    except Book.DoesNotExist:
        pass

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

    return render(
        request,
        'reviews/reviews.html',
        {
            'book': book,
            'reviews': reviews,
            'form': form,
        })
