from django.contrib import admin
from .models import Profile, Address

#Admin
admin.site.register(Profile)
admin.site.register(Address)