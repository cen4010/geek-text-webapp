from book_details.models import Book, Author, Publisher, Genre
import django_filters
from django_filters import OrderingFilter

#class to define filters for books, can be expanded to all fields of book
class bookFilter(django_filters.FilterSet):

    o = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('title', 'Book Title'),
            ('author', 'Author'),
            ('publish_date', 'Release Date'),
        ),
    )

    class Meta:
        model = Book
        fields = ['author', 'genre', ]
