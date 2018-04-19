from book_details.models import Book, Author, Publisher, Genre, Review
from carts.models import OrderItem
import django_filters
from django_filters import OrderingFilter
from django.db.models import Avg, Sum
from django.db.models.query import QuerySet

class CustomOrderingFilter(django_filters.OrderingFilter):

    def __init__(self, *args, **kwargs):
        super(CustomOrderingFilter, self).__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('avgRating', 'Lowest Rated'),
            ('-avgRating', 'Highest Rated'),
            ('topSeller', 'Top Sellers'),
        ]

    def avgRating(self,queryset,value):
        return queryset.annotate(avg_rating=Avg('reviews__rating')).filter(avg_rating__gte=value)

    def filter(self, qs, value):
        # OrderingFilter is CSV-based, so `value` is a list
        if any(v in ['avgRating'] for v in value):
            # sort queryset by rating
            return qs.annotate(avg_rating = Avg('reviews__rating')).order_by('avg_rating')

        if any(v in ['-avgRating'] for v in value):
            # sort queryset by rating
            return qs.annotate(avg_rating = Avg('reviews__rating')).order_by('-avg_rating')

        if any(v in ['topSeller'] for v in value):
            # sort queryset by topSeller
            return qs.annotate(top_seller = Sum('purchaed_book__quantity')).order_by('-top_seller')

        return super(CustomOrderingFilter, self).filter(qs, value)


#class to define filters for books, can be expanded to all fields of book
class bookFilter(django_filters.FilterSet):

    RATING_CHOICES = (
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★')
    )

    rating = django_filters.ChoiceFilter(name='reviews', lookup_expr='gte', method='avg_rating', choices=RATING_CHOICES)
    def avg_rating(self,queryset,name,value):
        return queryset.annotate(avg_rating=Avg('reviews__rating')).filter(avg_rating__gte=value)



    o = CustomOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'Book Title'),
            ('author', 'Author'),
            ('price', 'Price'),
            ('publish_date', 'Release Date'),
        ),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'rating']
