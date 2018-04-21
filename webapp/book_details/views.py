from django.shortcuts import render
from django.db.models import Avg

from .models import Book, Review
from .forms import ReviewForm
from carts.models import Order

def details(request, book_id):
    book = None
    reviews = None

    try:
        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book=book)
    except Book.DoesNotExist:
        pass

    if request.user.is_authenticated:
        try:
            review = Review.objects.get(book=book, user=request.user)
        except Review.DoesNotExist:
            review = Review(book=book, user=request.user)

        purchased = Order.objects.filter(user=request.user, orderItems__book=book).exists()
    else:
        review = None
        purchased = False

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm(instance=review)

    return render(request, 'book_details/details.html',
            {'book': book, 'reviews': reviews, 'form': form, 'purchased': purchased})
