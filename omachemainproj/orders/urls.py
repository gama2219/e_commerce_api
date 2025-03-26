from django.urls import path
from .views import create_order_view,webhook,view_orders_view

urlpatterns=[
    path('cashout/',create_order_view.as_view(),name='cashout'),
    path('safwebhook/',webhook.as_view(),name='hook'),
    path('track/order/',view_orders_view.as_view(),name='trackk')
]