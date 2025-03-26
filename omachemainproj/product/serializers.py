from rest_framework.serializers import(ModelSerializer,SerializerMethodField,Serializer,ListField,IntegerField)
from .models import product


class post_product_serializer(ModelSerializer):
    class Meta:
        model=product
        fields=('name',
                'image',
                'description',
                'category',
                'item_number',
                'price',
                'payment_mpesa_number')
        extra_kwargs={'description':{'required':False}}

    def create(self, validated_data):
        _=self.context['request'].user
        instance=product.objects.create(creator=_,**validated_data)
        return instance

class product_list_serializer(ModelSerializer):
    class Meta:
        model=product
        fields=('user_name',
                'name',
                'image',
                'description',
                'category',
                'price',
                'item_number',
                'id')
        
class product_home_serializer(ModelSerializer):
    electronics = SerializerMethodField()
    fashions = SerializerMethodField()
    kitchen = SerializerMethodField()
    computing = SerializerMethodField()
    gaming = SerializerMethodField()
    phonestablet = SerializerMethodField()

    class Meta:
        model=product
        fields=['electronics','fashions',
                'kitchen','computing',
                'gaming','phonestablet']
        
    def get_electronics(self,obj):
        _elctro=product.objects.filter(category='electronics').distinct()
        return product_list_serializer(_elctro,many=True,context=self.context).data
        
    def get_fashions(self,obj):
        _fashions=product.objects.filter(category='fashions').distinct()
        
        return product_list_serializer(_fashions,many=True,context=self.context).data

    def get_kitchen(self,obj):
        _kitchen=product.objects.filter(category='kitchen').distinct()
        return product_list_serializer(_kitchen,many=True,context=self.context).data

    def get_gaming(self,obj):
        _gaming=product.objects.filter(category='gaming').distinct()
        return product_list_serializer(_gaming,many=True,context=self.context).data

    def get_computing(self,obj):
        _computing=product.objects.filter(category='computing').distinct()
        return product_list_serializer(_computing,many=True,context=self.context).data

    def get_phonestablet(self,obj):
        _phonestablet=product.objects.filter(category='phonestablet').distinct()
        return product_list_serializer(_phonestablet,many=True,context=self.context).data
class idlistserializer(Serializer):
    ids=ListField(child=IntegerField(),allow_empty=False)




