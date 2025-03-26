from django.contrib import admin
from .models import order_payment,order_track
# Register your models here.
admin.site.register(order_payment)
admin.site.register(order_track)

