from django.conf.urls import url
from . import views
#Users
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
  
]