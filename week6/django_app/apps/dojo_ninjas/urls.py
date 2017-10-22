from django.conf.urls import url
from . import views
#Surveys
urlpatterns = [
    url(r'^$', views.index),
 
]