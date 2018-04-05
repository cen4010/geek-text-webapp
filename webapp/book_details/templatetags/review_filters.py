from django import template
from django.db.models import Avg
from django.utils.safestring import mark_safe

from book_details.models import Review

register = template.Library()

@register.filter
def get_stars(rating):
    if rating is None:
        return 'No rating'

    return mark_safe(('<div class="rating">'
        '<div class="empty-stars">'
        '<span class="glyphicon glyphicon-star-empty"></span>'
        '<span class="glyphicon glyphicon-star-empty"></span>'
        '<span class="glyphicon glyphicon-star-empty"></span>'
        '<span class="glyphicon glyphicon-star-empty"></span>'
        '<span class="glyphicon glyphicon-star-empty"></span>'
        '</div>'
        '<div class="full-stars" style="width:{}%;">'
        '<span class="glyphicon glyphicon-star"></span>'
        '<span class="glyphicon glyphicon-star"></span>'
        '<span class="glyphicon glyphicon-star"></span>'
        '<span class="glyphicon glyphicon-star"></span>'
        '<span class="glyphicon glyphicon-star"></span>'
        '</div>'
        '</div>').format(rating / 5 * 100))

@register.filter
def avg_rating(book):
    reviews = Review.objects.filter(book=book)
    return get_stars(reviews.aggregate(Avg('rating'))['rating__avg'])
