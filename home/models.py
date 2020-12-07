from django.db import models


# Create your models here.
class categories(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
                            max_length=20,
                            null=False,
                            blank=False
                            )
    image_url = models.CharField(
                            max_length=500,
                            null=False,
                            blank=False
                            )
    image_id = models.CharField(
                            max_length=500
                            )

    def __str__(self):
        return self.name


class SocialMedia(models.Model):

    class Meta:
        verbose_name_plural = 'Social Media'

    name = models.CharField(
                            max_length=10,
                            null=False,
                            blank=False
                            )
    site_url = models.URLField(
                            max_length=1024,
                            null=False,
                            blank=False
                            )
    icon = models.CharField(
                            max_length=500,
                            null=False,
                            blank=False
                            )

    def __str__(self):
        return self.name
