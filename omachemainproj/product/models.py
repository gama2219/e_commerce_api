from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


#category of product
choices=[('electronics','electronics'),
('furniture','furniture'),
('fashions','fashions'),
('kitchen','kitchen'),
('appliance','appliance'),
('computing','computing'),
('gaming','gaming'),
('phones$tablet','phones$tablet'),
('sports','sports'),
]


# Create your models here.
class product(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator_post')
    name=models.CharField( blank=True,max_length=50)
    image=models.ImageField(upload_to='post',validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])],null=True,blank=True)
    description=models.TextField()
    category=models.CharField(choices=choices,max_length=15,blank=True)
    price=models.IntegerField(default=0)
    item_number=models.IntegerField(null=True)
    soldout=models.BooleanField(default=False)
    payment_mpesa_number=models.IntegerField(default=254123456789)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def user_name(self):
        username=self.creator.username
        return f'{username}'

    def __str__(self):
        return f"{self.creator.username} post a new product on {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']
