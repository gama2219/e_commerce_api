from django.db import models
from django.contrib.auth.models import User
from product.models import product
import uuid


# Create your models here.

trackstatus=[('created','created'),('paid','paid'),
             ('fetched','fetched'),('shipping','shipping'),
             ('deliverd','deliverd')]

payment_stat=[('requested','requested'),('paid','paid')]


class order_payment(models.Model):
    order_token=models.CharField(max_length=37,unique=True,editable=False,default=uuid.uuid4())
    mpesa_phone=models.IntegerField()
    payment_status=models.CharField(choices=payment_stat,max_length=20)

    @property
    def order_amount(self):
        total_amount_price=sum([_.tt_amount for _ in self.pay_ment])
        return total_amount_price


    def __str__(self):
        if self.payment_status == 'requested':
            return f'{self.order_token} is succsefull {self.payment_status}'
        elif self.payment_status =='paid':
            return f'{self.order_token} is succsefull {self.payment_status}'
        else:
            return super().__str__()
        

class order_track(models.Model):
    pro_duct=models.ForeignKey(product,on_delete=models.CASCADE,related_name='pro_duct')
    buyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='buyer')
    payment=models.ForeignKey(order_payment,on_delete=models.CASCADE,related_name='pay_ment',null=True)
    number=models.IntegerField()
    track_status=models.CharField(choices=trackstatus ,max_length=20,default='created')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def seller(self):
        sella=self.pro_duct.user_name
        return sella
    
    @property
    def tt_amount(self):
        _amount=self.pro_duct.price * self.number

        return _amount
    

    def __str__(self):
        return f"{self.buyer} is buying {self.pro_duct.name}"


