from django.contrib import admin
from .models import Profile, Address, CreditCard

#Admin
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(CreditCard)