from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# @login_required(login_url="not_account")
def books(request):
    paginator = Paginator(Book.objects.all(), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': Book.objects.all(),
        'page_obj': page_obj
    }
    return render(request, 'books/books.html', context)


# @login_required(login_url="not_account")
def bookDetail(request, pk):
    context = {
        'book': Book.objects.get(id=pk)
    }
    return render(request, 'books/book.html', context)