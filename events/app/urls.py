from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.viewer),
    url(r'^events/$', views.get_events),
    url(r'^events/add/$', views.add_event)
]
