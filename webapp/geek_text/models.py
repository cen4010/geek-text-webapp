from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=8)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

