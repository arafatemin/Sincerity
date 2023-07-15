from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('articles', articles, name='articles'),
    path('Article_Detail/<int:id>', article_detail, name='Article_Detail'),
    path('getArticle/<str:id>/', getArticle, name='getarticles'),
]