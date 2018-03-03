from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Using direct User model due to issues with Seeder
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey(
        'book_details.Book',
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
