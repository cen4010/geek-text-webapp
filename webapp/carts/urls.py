from django.conf.urls import url

from .views import (
    cart_home,
    cart_add_book,
    cart_remove_book,
    cart_update_quantity,
    cart_checkout,
    cart_checkout_home
)

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^add/$', cart_add_book, name='add'),
    url(r'^remove/$', cart_remove_book, name='remove'),
    url(r'^update_quantity/$', cart_update_quantity, name='update_quantity'),
    url(r'^checkout/$', cart_checkout, name='checkout_action'),
    url(r'^checkout_home/$', cart_checkout_home, name='checkout_home')
]
