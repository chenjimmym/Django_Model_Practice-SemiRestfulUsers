from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'users$', views.users),
    url(r'users/(?P<user_number>\d+)', views.show),
    url(r'users/new$', views.new),
    url(r'users/create$', views.create),
    url(r'users/delete(?P<user_number>\d+)$', views.delete),
    url(r'users/edit(?P<user_number>\d+)$', views.edit),
    url(r'users/update(?P<user_number>\d+)$', views.update),
]