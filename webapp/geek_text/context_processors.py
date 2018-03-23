from django.conf import settings
from browse.filters import bookFilter
from book_details.models import Book

#this provides the filter context required for the search bar
def searchBar(request):
    qs = Book.objects.all()
    filtered = bookFilter(request.GET, queryset=qs)

    return {'filter': filtered}
