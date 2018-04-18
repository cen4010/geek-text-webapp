from django.shortcuts import render
from django.http import HttpResponse
from book_details.models import Book, Author, Publisher, Genre, Review
from django.views.generic import ListView
from .filters import bookFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import filters
from django.db.models import Avg, Sum

# Create your views here.
def browse(request):

    qs = Book.objects.annotate(top_seller = Sum('purchaed_book__quantity')).order_by('-top_seller')

    filtered = bookFilter(request.GET, queryset=qs)
    qs = filtered.qs


    #How many results does the user want to see?
    per_page = int(request.GET.get('p',10))

    paginator = Paginator(qs, per_page)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)


    return render(
        request,
         'browse/browse.html', {'books': books, 'filter': filtered }
        #context={'bookList':bookList, 'fantasyList':fantasyList, 'scifiList':scifiList, 'genreList': genreList}
    )
