from django import template
from django.db.models import Avg

from book_details.models import Review

register = template.Library()

@register.filter
def get_stars(rating):
    stars = {
        1: '★☆☆☆☆',
        2: '★★☆☆☆',
        3: '★★★☆☆',
        4: '★★★★☆',
        5: '★★★★★'
    }

    if rating is None:
        return None

    return stars.get(round(rating))


@register.filter
def avg_rating(book):
    reviews = Review.objects.filter(book=book)
    return get_stars(reviews.aggregate(Avg('rating'))['rating__avg'])

