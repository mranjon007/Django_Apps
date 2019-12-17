from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('book/create/', book_create, name='book-create'),
]