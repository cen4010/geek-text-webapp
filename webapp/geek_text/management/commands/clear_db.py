
from django.core.management.base import BaseCommand

from django_seed import Seed

from django.contrib.auth.models import User
from book_details.models import Book, Author, Publisher, Genre
from reviews.models import Review

class Command(BaseCommand):
    help = 'Clears all models from the local DB'

    def handle(self, *args, **options):
        # Reviews
        Review.objects.all().delete()

        # Book Details
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Genre.objects.all().delete()

        # User
        User.objects.all().delete()
