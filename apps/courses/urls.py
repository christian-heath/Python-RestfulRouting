from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses$', views.index),
    url(r'^courses/add$', views.add),
    url(r'^courses/confirm_destroy/(?P<id>\d+)$', views.confirm),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy)
]