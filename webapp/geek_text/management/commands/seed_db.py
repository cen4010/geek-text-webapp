from django.core.management.base import BaseCommand

from django_seed import Seed

from django.contrib.auth.models import User
from book_details.models import Book, Author, Publisher, Genre
from reviews.models import Review

class Command(BaseCommand):
    help = 'Seeds the local DB by adding model instances'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        # User
        seeder.add_entity(User, 15)

        # Book Details
        seeder.add_entity(Author, 15)
        seeder.add_entity(Publisher, 15)
        seeder.add_entity(Genre, 15)
        seeder.add_entity(Book, 15)

        # Reviews
        seeder.add_entity(Review, 15)

        seeder.execute()
