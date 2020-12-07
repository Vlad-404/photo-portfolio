from django.db import models


# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=30),
    description = models.TextField(),
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL),
    panorama = models.BooleanField(default=False),
    color = models.BooleanField(default=False),
    price = models.DecimalField(max_digits=6, decimal_places=2),
    rating = models.DecimalField(max_length=6, decimal_places=2, null=False, blank=False),
    imgurl = models.URLField(max_length=1024, null=True, blank=True),
    imgid = models.CharField(max_length=126, null=True, blank=True),
    notes = models.CharField(max_length=254, null=False, blank=False),
    uploaded_by = models.CharField(max_length=50, null=False, blank=False),

    def __str__(self):
        return self.title
