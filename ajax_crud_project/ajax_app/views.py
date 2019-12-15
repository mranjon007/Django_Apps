from django.shortcuts import render
from .models import *


def book_list(request):
    books = Book.objects.all()
    return render(request, template_name='ajax_app/book_list.html', context={'books': books})


