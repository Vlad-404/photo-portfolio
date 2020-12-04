from django.db import models


# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    image_url = models.CharField(max_length=500, null=False, blank=False)
    image_id = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    site_url = models.CharField(max_length=500, null=False, blank=False)
    icon = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
