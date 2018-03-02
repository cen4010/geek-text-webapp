from django.conf.urls import url
from .import views
from django.contrib.auth.views import (
    login, logout,
    password_reset, password_change_done,
    password_reset_confirm
)


urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login , {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout , {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$' , views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile' ),
    url(r'^profile/edit/$', views.edit_profile,
        name='edit_profile'),
    url(r'^change_password/$', views.change_password,
            name='change_password'),
    url(r'^reset_password/$', password_reset , name='reset_password'),
    url(r'^reset_password/done/$', password_change_done,name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,name='password_reset_confirm')
]