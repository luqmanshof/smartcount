from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    job_description  = models.CharField(blank=True,max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    image = models.ImageField(upload_to='images/profilepix/', blank=True)
    signature = models.ImageField(upload_to='images/signature/', blank=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class ChartCategory(models.Model):
    category_code = models.PositiveSmallIntegerField()
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return self.category_name

class ChartSubCategory(models.Model):
    category_code = models.ForeignKey(ChartCategory,on_delete=models.CASCADE)
    sub_category_code = models.PositiveIntegerField()
    sub_category_name = models.CharField(max_length=256)
    notes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.sub_category_name





# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
