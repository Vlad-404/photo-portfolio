from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Imports so it can receive data from signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    # Specifies that each user can have only one profile
    user = models.OneToOneField(
                            User,
                            on_delete=models.CASCADE)
    # Adds values for storing
    default_phone_number = models.CharField(
                                max_length=20,
                                null=True,
                                blank=True,
                                )
    default_country = CountryField(
                                blank_label='Country *',
                                max_length=20,
                                null=True,
                                blank=True
                                )
    default_postcode = models.CharField(
                                max_length=20,
                                null=True,
                                blank=True,
                                default=''
                                )
    default_town_or_city = models.CharField(
                                max_length=40,
                                null=True,
                                blank=True
                                )
    default_street_address1 = models.CharField(
                                max_length=80,
                                null=True,
                                blank=True
                                )
    default_street_address2 = models.CharField(
                                max_length=80,
                                null=True,
                                blank=True
                                )
    default_county = models.CharField(
                                max_length=80,
                                null=True,
                                blank=True
                                )

    def __str__(self):
        return self.user.name


# Create or update user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    # For existing users, just saves the profile
    instance.userprofile.save()
