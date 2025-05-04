from django.contrib import admin
from .models import product
from unfold.admin import ModelAdmin
# Register your models here.
#admin.site.register(product)


@admin.register(product)
class CustomAdminClass(ModelAdmin):
    pass