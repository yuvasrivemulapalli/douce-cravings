from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Details(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.CharField(default="User", max_length=50)
    gender = models.CharField(default="Other", max_length=20)

@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        Details.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_details(sender, instance, **kwargs):
    instance.details.save()
