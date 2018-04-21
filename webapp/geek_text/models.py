from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from localflavor.us.models import USStateField, USZipCodeField


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=16, default='', null=True)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='address')
    address = models.CharField(max_length=25, blank=True,
                               null=True, default='')
    state = USStateField()
    city = models.CharField(max_length=12,
                            null=True)
    zipcode = USZipCodeField()

    def __str__(self):
        return self.user.username


