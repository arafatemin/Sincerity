from django.core.paginator import Paginator
from django.shortcuts import render

from Projects.forms import ContactForm
from .models import *
from Projects.models import *
from Books.models import *
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')

    context = {
        'managers': Manager.objects.all(),
        'projects': Project.objects.all(),
        'books': Book.objects.all(),
        'articles': Article.objects.all(),
        'categories': Category.objects.order_by("-title").all()[:3],
        'educations': Education.objects.all(),
        'form': ContactForm()
    }
    return render(request, 'index.html', context)


# @login_required(login_url="not_account")
def articles(request):
    paginator = Paginator(Category.objects.all(), 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': Category.objects.all(),
        'page_obj': page_obj
    }
    return render(request, 'Articles/articles.html', context)


# @login_required(login_url="not_account")
def article_detail(request, id):
    category = request.GET.get("category")
    if category == None:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category__title=category)

    context = {
        'articles': articles,
        'groups': Group.objects.filter(category__title=category),
        'category': category,  # Title Gostermek icin or: The Django information
    }
    return render(request, 'Articles/article_detail.html', context)


def getArticle(reqest, id):
    article_name = reqest.GET.get("category")
    article = Article.objects.get(id=id)
    context = {
        'article': article,
        'article_name': article_name,
        'all_articles': SubCategory.objects.filter(article__name=article.name, category__title=article.category.title),
    }
    return render(reqest, "Articles/getArticle.html", context)
