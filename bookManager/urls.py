from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('authors', views.showAuthors, name='authors'),
    path('books', views.showBooks, name='books')
]