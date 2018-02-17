from django.shortcuts import render
from django.http import HttpResponse
from book_details.models import Book, Author, Publisher, Genre
from django.views.generic import ListView
from .filters import bookFilter

# Create your views here.
def browse(request):

    bookList = Book.objects.all()

    book_filter = bookFilter(request.GET, queryset=bookList)

    return render(
        request,
         'browse.html', {'filter': book_filter}
        #context={'bookList':bookList, 'fantasyList':fantasyList, 'scifiList':scifiList, 'genreList': genreList}
    )
