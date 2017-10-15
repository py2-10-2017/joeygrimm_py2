from django.conf.urls import url

from . import views # This imports the views file from the same folder this file is saved in

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^process$', views.process),
    
]

