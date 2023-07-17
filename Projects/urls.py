from django.urls import path
from .views import *

urlpatterns = [
    path('school', school, name='school'),
    path('course', course, name='course'),
    path('experience', experience, name='experience'),
    path('projects', project, name='project'),
    path('aboutme', AboutMe.as_view(), name='aboutMe'),
    path('contact', contact, name='contact'),
    path('not_account', not_account, name='not_account'),
]

