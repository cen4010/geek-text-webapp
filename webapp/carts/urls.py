from django.conf.urls import url

from .views import (
        cart_home, 
        cart_add_book,
        cart_remove_book
        )

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^add/$', cart_add_book , name='add'),
    url(r'^remove/$', cart_remove_book , name='remove'),
]

