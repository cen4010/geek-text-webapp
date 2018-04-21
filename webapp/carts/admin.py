from django.contrib import admin
from .models import Cart,CartItem,OrderItem,Order,SavedItems

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SavedItems)
