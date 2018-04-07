from book_details.models import Book, Author, Publisher, Genre
import django_filters
from django_filters import OrderingFilter
from django.db.models import Avg

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
        return queryset.annotate(avg_rating=Avg('reviews__rating')).filter(avg_rating=value)

    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'Book Title'),
            ('author', 'Author'),
            ('publish_date', 'Release Date'),
            ('reviews__rating', 'Average Rating'),
        ),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'rating']
