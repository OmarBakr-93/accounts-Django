from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)    
def create_profile(sender , instance , created , **kwargs):
        if created:
            Profile.objects.create(
                user=instance
            )