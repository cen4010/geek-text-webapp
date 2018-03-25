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
                user_cart = self.model.objects.filter(user=request.user).first()
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
    book = models.ForeignKey('Relative to the book',Book, related_name='book')
    quantity = models.IntegerField('quantity of books',default=1)
    price = models.DecimalField('Temp: Price of book',max_digits=6, decimal_places=2, blank=True, null=True)
    book_price_quantity = models.DecimalField('Price of Line Item: BookPricexQuantity',max_digits=8, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return str(self.id)


# Tied the cart to the user for persistance for when a user signs in they want to acess their cart.
class Cart(models.Model):
    user = models.ForeignKey('Cart Owner',User, null=True, blank=True)
    cartItems = models.ManyToManyField('Items to go into cart',CartItem, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField('Last Change to Cart',auto_now=True)
    timestamp = models.DateTimeField('Time of Cart Creation',auto_now_add=True)
    objects = CartsManager()

    def __str__(self):
        return str(self.id)

#useed to create the total value when the cart recieves changes https://docs.djangoproject.com/en/2.0/ref/signals/
def m2m_changed_cart(sender, instance, action,**kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        cartItems = instance.cartItems.all()
        total = 0
        for x in cartItems:
            total += x.price*x.quantity
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart, sender=Book)

