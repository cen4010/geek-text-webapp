from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed

from book_details.models import Book
User = settings.AUTH_USER_MODEL

# cart manager is used to create new carts based on session and user information https://docs.djangoproject.com/en/2.0/topics/db/managers/


class CartsManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                user_cart = self.model.objects.filter(
                    user=request.user).first()
                if user_cart is not None:
                    cart_obj.cartItems.add(*user_cart.cartItems.all())
                    cart_obj.user = request.user
                    cart_obj.save()
                    user_cart.delete()
                else:
                    cart_obj.user = request.user
                    cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                cart_obj = self.model.objects.filter(user=user).first()
                if cart_obj is not None:
                    return cart_obj
                user_obj = user
        return self.model.objects.create(user=user_obj)

# cartItems realte to the Cart to support multiple items


class CartItem(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='book')
    quantity = models.IntegerField(
        'quantity of books',
        default=1)
    price = models.DecimalField(
        'Price of book',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True)

    def __str__(self):
        return str(self.id)



class SavedItems(models.Model):
    book = models.ForeignKey(Book)

    def __str__(self):
        return self.book.title


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True)
    cartItems = models.ManyToManyField(
        CartItem,
        blank=True)
    subtotal = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    total = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    updated = models.DateTimeField(
        'Last Change to Cart',
        auto_now=True)
    timestamp = models.DateTimeField(
        'Time of Cart Creation',
        auto_now_add=True)
    objects = CartsManager()

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='purchaed_book')
    quantity = models.IntegerField(
        'quantity of books',
        default=1)
    price = models.DecimalField(
        'Price of book',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True)
    book_price_quantity = models.DecimalField(
        'Price of Line Item: BookPrice*Quantity',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.id, self.book, self.quantity)


class Order(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True)
    orderItems = models.ManyToManyField(
        OrderItem,
        blank=True)
    subtotal = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    total = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)

    def __str__(self):
        return str(self.id)
