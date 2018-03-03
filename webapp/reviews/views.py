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

    if request.method == 'POST':
        review = Review(book=book, user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    return render(
        request,
        'reviews/reviews.html',
        {
            'book': book,
            'reviews': reviews,
            'form': form,
            'average_rating' : average_rating
        })
