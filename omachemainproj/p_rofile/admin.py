from django.contrib import admin
from .models import Pprofile
from unfold.admin import ModelAdmin
# Register your models here.

#admin.site.register(Pprofile)

@admin.register(Pprofile)
class CustomAdminClass(ModelAdmin):
    pass