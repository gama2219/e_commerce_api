from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .models import Pprofile
from .serializers import account_profile_serializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class account_profile_view(RetrieveUpdateDestroyAPIView):
    queryset=Pprofile.objects.all()
    serializer_class=account_profile_serializer
    permission_classes=[IsAuthenticated]

    #ovaride the get_bbject function to filter the account profile based on the authenticated user
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset,user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj
