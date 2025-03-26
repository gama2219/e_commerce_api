from django.urls import path
from .views import account_profile_view


urlpatterns=[
    path('account/',account_profile_view.as_view(),name='account'),
]
