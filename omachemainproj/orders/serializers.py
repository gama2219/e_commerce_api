from rest_framework.serializers import Serializer,ModelSerializer,IntegerField,ImageField,CharField
from .models import order_track,order_payment



class order_track_serializer(ModelSerializer):
    class Meta:
        model=order_track
        fields=('pro_duct','number')
        extra_kwargs ={field.name:{'required':False} for field in model._meta.fields}


class orders_create_serializer(Serializer):
    order = order_track_serializer(many=True)
    mpesa_number = IntegerField()
    
    def create(self, validated_data):
        buyer = self.context['request'].user
        order_data = validated_data.get('order')
        mpesa_num=validated_data.get('mpesa_number')
        
        # Create the order payment instance
        order_payment_instance = order_payment.objects.create(
            mpesa_phone=validated_data.pop('mpesa_number')
        )
        
        # Create order track objects
        order_list_objects = [
            order_track.objects.create(payment=order_payment_instance, buyer=buyer, **items) 
            for items in order_data
        ]
        
        # Return the order_payment_instance instead of the list
        return {"order": order_list_objects, "mpesa_number": mpesa_num}

    





class oder_view_serializer(ModelSerializer):
    name=CharField(source='pro_duct.name')
    avatar=ImageField(source='pro_duct.image')

    class Meta:
        model=order_track
        fields=['name','avatar','number','track_status','created_at']
        
    