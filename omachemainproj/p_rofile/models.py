from django.db import models
from django.contrib.auth.models import User



choices=[
    ('male','male'),
    ('female','female')
]
# Create your models here.
class Pprofile (models.Model):
        
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="userprofile")
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=1000, default='no bio ....')
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='', upload_to='avatars/',blank=True)
    gender =models.CharField(choices=choices,max_length=10,blank=True)
    #slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def user_name(self):
        return self.user.username

    def __str__(self):
        return f"{self.user.username} has created profile on {self.created}"