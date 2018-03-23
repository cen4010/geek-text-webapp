from book_details.models import Book, Author, Publisher, Genre
from reviews.models import Review
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
        fields = ['title', 'author', 'genre']


#class ratingFilter(django_filters.FilterSet):

#    class Meta:
#        model = Review
#        fields = ['comment' ]
