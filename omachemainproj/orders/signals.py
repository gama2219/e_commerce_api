from .models import order_payment,order_track
from django.db.models.signals import post_save
from django.dispatch import receiver 
    
@receiver(post_save,sender=order_track)
def make_payment_signal(sender,instance,created,**kwargs):
    if created:
        match instance.track_status:
            case "created":
                bought_item=instance.number
                available_item=instance.pro_duct.item_number
                #update product amounnt after succsessful purchase
                instance_=instance.pro_duct
                instance_.item_number=available_item-bought_item
                instance_.save()
    if not created:
            match instance.track_status:
                case "fetched":
                    #mpesa send money to seller
                    print("send money to seller")

@receiver(post_save,sender=order_payment)
def make_payment_signal(sender,instance,created,**kwargs):
    if created:
        print("handle payment from buyer")
