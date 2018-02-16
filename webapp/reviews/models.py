from django.conf import settings
from django.db import models

class Review(models.Model):
    book = models.ForeignKey(
        'book_details.Book',
        related_name='reviews')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviews')
    anonymous = models.BooleanField(
        'Anonymous')
    rating = models.IntegerField(
        'Rating',
        null=True,
        blank=True,
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        ])
    comment = models.TextField(
        'Comment',
        max_length=500,
        blank=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return '{} -- {}'.format(self.book.title, self.user.username)
