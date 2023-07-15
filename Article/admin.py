from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "category")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "article", "category")

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Article, ArticleAdmin)
