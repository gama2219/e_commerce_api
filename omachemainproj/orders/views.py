from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView
from .serializers import orders_create_serializer,oder_view_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import order_track
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.

class create_order_view(CreateAPIView):
    serializer_class=orders_create_serializer
    queryset=order_track.objects.all()

    

class view_orders_view(ListAPIView):
    serializer_class = oder_view_serializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return order_track.objects.filter(buyer=self.request.user.id)


class webhook(APIView):
    def post(self,request,*args,**kwargs):
        try:
            data=request.data
            #logic after success payment
            return Response({'status':"success"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':"error"},status=status.HTTP_417_EXPECTATION_FAILED)



