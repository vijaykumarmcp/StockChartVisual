from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .import views

urlpatterns = [
    path('list/',views.list_view,name='list'),
    path('create/',views.create_view,name='create'),
    url(r'^(?P<id>\d+)/delete/',views.delete_view,name='delete'),
]
