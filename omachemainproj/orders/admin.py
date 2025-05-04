from django.contrib import admin
from .models import order_payment,order_track
from unfold.admin import ModelAdmin
# Register your models here.
#admin.site.register(order_payment)
#admin.site.register(order_track)

@admin.register(order_payment)
class CustomAdminClass(ModelAdmin):
    pass

@admin.register(order_track)
class CustomAdminClass(ModelAdmin):
    pass
