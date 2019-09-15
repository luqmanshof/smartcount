from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description  = models.CharField(blank=True,max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    image = models.ImageField(upload_to='images/profilepix/', blank=True)
    signature = models.ImageField(upload_to='images/signature/', blank=True)

    def __str__(self):
        return self.user.username
