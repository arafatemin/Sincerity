from django.urls import path
from .views import *
urlpatterns = [
    path('books/', books, name='books'),
    path('bookDetail/<str:pk>/', bookDetail, name='bookDetail'),

]