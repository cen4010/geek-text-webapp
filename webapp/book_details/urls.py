"""geek_text book_details URL Configuration
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<book_id>(0|[1-9][0-9]*))/', views.details),
]
