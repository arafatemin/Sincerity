from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import handler404
from django.urls import re_path as url
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Article.urls')),
    path('', include('Projects.urls')),
    path('', include('user.urls')),
    path('', include('Photos.urls')),
    path('', include('Books.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = 'Projects.views.handler404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
