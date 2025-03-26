from django.shortcuts import render
from rest_framework.generics import (CreateAPIView,ListAPIView)
from .serializers import post_product_serializer,product_list_serializer,product_home_serializer,idlistserializer
from rest_framework import filters
from .models import *
from .paginationn import fetch_pagination
from rest_framework.response import Response
from rest_framework import status,viewsets

# Create your views here.

class createproduct_post(CreateAPIView):
    queryset=product.objects.all()
    serializer_class=post_product_serializer
    

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class search_product(ListAPIView):
    queryset=product.objects.all()
    serializer_class=product_list_serializer
    filter_backends=[filters.SearchFilter]
    search_fields=['name']
    pagination_class=fetch_pagination

class product_electonics_view(ListAPIView):
    queryset=product.objects.all().filter(category='electronics',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_furniture_view(ListAPIView):
    queryset=product.objects.all().filter(category='furniture',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_fashions_view(ListAPIView):
    queryset=product.objects.all().filter(category='fashions',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_computing_view(ListAPIView):
    queryset=product.objects.all().filter(category='computing',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_gaming_view(ListAPIView):
    queryset=product.objects.all().filter(category='gaming',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_kitchen_view(ListAPIView):
    queryset=product.objects.all().filter(category='kitchen',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_phones_tablet_view(ListAPIView):
    queryset=product.objects.all().filter(category='phones$tablet',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class product_sports_view(ListAPIView):
    queryset=product.objects.all().filter(category='sports',soldout=False)
    serializer_class=product_list_serializer
    pagination_class=fetch_pagination

class home_view(ListAPIView):
    queryset=product.objects.all().filter(soldout=False)
    serializer_class=product_home_serializer

class cart_view(viewsets.ViewSet):

    def create(self, request):
        serializer=idlistserializer(data=request.data)
        if serializer.is_valid():
            ids=serializer.validated_data['ids']
            filterd_results=product.objects.filter(id__in=ids)
            serializer=product_list_serializer(filterd_results,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        