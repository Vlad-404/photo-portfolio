from django.db import models
from home.models import Categories


# Create your models here.
class Images(models.Model):

    class Meta:
        verbose_name_plural = 'Images'

    title = models.CharField(
                            max_length=30,
                            default=None,
                            null=False,
                            blank=False
                            )
    description = models.TextField(
                            default=None
                            )
    category = models.ForeignKey(
                            Categories,
                            default=None,
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL
                            )
    panorama = models.BooleanField(
                            null=False,
                            blank=False,
                            default=False
                            )
    color = models.BooleanField(
                            null=False,
                            blank=False,
                            default=False
                            )
    price = models.DecimalField(
                            max_digits=6,
                            decimal_places=2,
                            default=None
                            )
    rating = models.DecimalField(
                            max_digits=6,
                            decimal_places=2,
                            null=False,
                            blank=False,
                            default=None
                            )
    imgurl = models.URLField(
                            max_length=1024,
                            null=False,
                            blank=False,
                            default=None
                            )
    imgid = models.CharField(
                            max_length=126,
                            null=True,
                            blank=True,
                            default=None
                            )
    image = models.ImageField(
                            null=True,
                            blank=True,
                            default=None
                            )
    notes = models.TextField(
                            default=None
                            )
    uploaded_by = models.CharField(
                            max_length=30,
                            default=None
                            )

    def __str__(self):
        return self.title
