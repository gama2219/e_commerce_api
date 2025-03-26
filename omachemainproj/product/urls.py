from django.urls import path
from .views import *

urlpatterns=[
    path('create/',createproduct_post.as_view(),name='create'),
    path('product/search/',search_product.as_view(),name='product_list'),
    path('product/electronics/',product_electonics_view.as_view(),name='electronics'),
    path('product/furniture/',product_furniture_view.as_view(),name='furniture'),
    path('product/fashions/',product_fashions_view.as_view(),name='fashions'),
    path('product/computing/',product_computing_view.as_view(),name='computing'),
    path('product/gaming/',product_gaming_view.as_view(),name='gaming'),
    path('product/kitchen',product_kitchen_view.as_view(),name='kitchen'),
    path('product/phones/',product_phones_tablet_view.as_view(),name='phones'),
    path('product/sports/',product_sports_view.as_view(),name='sports'),
    path('',home_view.as_view(),name='home'),
    path('cart/',cart_view.as_view({'post':'create'}),name='cart')
]