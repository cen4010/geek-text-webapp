from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    #allowed nulls and blanks for future guest checkout
    user = models.ForeignKey(
        User,
        null=True,
        blank=True)

    book = models.ForeignKey(
        'book_details.Book',
        related_name='product')

    total_price = models.DecimalField(
        'total price of all items',
        default=0.00,
        max_digits=100,
        decimal_places=2)

    updated = models.DateTimeField(
        auto_now=True)

    timestamp = models.DateTimeField(
        auto_now_add=True)

    quantity = models.IntegerField(
        'quanitity of books',
        default=1)

    book_price_quantity = models.DecimalField(
        'intermediate of price per book*quantity',
        max_digits=5,
        decimal_places=2,
        default=0)

    def __str__(self):
        return str(self.user)
