from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money

# Using direct User model due to issues with Seeder
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(
        'Title of the book',
        max_length=255)
    author = models.ForeignKey(
        'Author',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    description = models.TextField(
        'Description of book contents and misc info',
        max_length=500,
        blank=True)
    price = MoneyField(
        'Price',
        max_digits=20,
        decimal_places=2,
        default_currency='USD',
        default=Money(0, 'USD'))
    genre = models.ForeignKey(
        'Genre',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        'Publisher',
        related_name='books',
        null=True,
        on_delete=models.SET_NULL)
    publish_date = models.DateField(
        'Date publisher initially released current book version')
    cover = models.ImageField(
        'Front cover of book',
        upload_to = 'book_covers/',
        null=True)

    def __str__(self):
        return '{} -- {}'.format(self.author, self.title)

class Author(models.Model):
    name = models.CharField(
        'Name of author',
        max_length=255)
    bio = models.TextField(
        'Short biography of author and description of work',
        max_length=500,
        blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Publisher(models.Model):
    name = models.CharField(
        'Name of publishing company',
        max_length=255)
    location = models.CharField(
        'Street address of publishing company',
        max_length=255,
        blank=True)
    website = models.URLField(
        'Publisher home webpage',
        blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Genre(models.Model):
    name = models.CharField(
        'Short name for genre',
        max_length=16)

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):
    book = models.ForeignKey(
        'Book',
        related_name='reviews')
    user = models.ForeignKey(
        User,
        related_name='reviews')
    anonymous = models.BooleanField(
        'Whether or not the comment was posted anonymously')
    rating = models.IntegerField(
        'Rating associated with user comment; implies a review of the Book',
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(
        'User submitted comment on the associated Book',
        max_length=500,
        blank=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return '{} -- {}'.format(self.book.title, self.user.username)
