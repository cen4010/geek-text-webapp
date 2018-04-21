from django.conf.urls import url

from .views import (
    cart_home,
    cart_add_book,
    cart_remove_book,
    cart_update_quantity,
    cart_save_for_later,
    cart_delete_from_saved,
    cart_add_back,
    cart_checkout,
    cart_checkout_home,
)

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^add/$', cart_add_book, name='add'),
    url(r'^remove/$', cart_remove_book, name='remove'),
    url(r'^update_quantity/$', cart_update_quantity, name='update_quantity'),
    url(r'^update_save/$', cart_save_for_later, name='save_for_later'),
    url(r'^remove_save/$', cart_delete_from_saved, name='delete_save'),
    url(r'^add_back/$', cart_add_back, name='add_back'),
    url(r'^checkout/$', cart_checkout, name='checkout_action'),
    url(r'^checkout_home/$', cart_checkout_home, name='checkout_home')
]
