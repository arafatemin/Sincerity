from django.urls import path
from .views import *
urlpatterns = [
    path('gallery/', gallery, name='gallery'),
    path('add/', addphoto, name='add')

]