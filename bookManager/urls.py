from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('authors', views.list_Authors, name='authors'),
    path('books', views.list_books, name='books'),
    path('authors/<int:author_id>', views.show_authors, name='showAuthor'),
    path('books/<str:book_id>', views.show_books, name='showBooks'),
    path('authors<int:author_id>/delete', views.delete_author, name='delteAuthor'),
    path('books<str:book_id>/delete', views.delete_book, name='delteBooks'),
]