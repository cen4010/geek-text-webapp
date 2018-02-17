from book_details.models import Book, Author, Publisher, Genre
import django_filters

#class to define filters for books, can be expanded to all fields of book
class bookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['author', 'genre', ]
