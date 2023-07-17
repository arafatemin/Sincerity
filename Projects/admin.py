from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .models import *


@csrf_exempt
class MyAdminView(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Project, MyAdminView)
admin.site.register(Manager, MyAdminView)
admin.site.register(Experience, MyAdminView)
admin.site.register(Education, MyAdminView)
admin.site.register(CategoryEducation, MyAdminView)
admin.site.register(Contact, MyAdminView)
