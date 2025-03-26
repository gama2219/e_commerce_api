from .models import Pprofile
from rest_framework.serializers import ModelSerializer,ValidationError




class account_profile_serializer(ModelSerializer):
    class Meta:
        model=Pprofile
        fields=('first_name',
                "last_name",
                'bio',
                'avatar',
                'gender')
        extra_kwargs ={field.name:{'required':False} for field in model._meta.fields}


