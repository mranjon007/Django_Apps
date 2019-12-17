from django.shortcuts import render
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse


def book_list(request):
    books = Book.objects.all()
    return render(request, template_name='ajax_app/book_list.html', context={'books': books})


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('books/includes/partial_book_create.html',
        context,
        request=request
    )
    return JsonResponse(data)

