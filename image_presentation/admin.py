from django.contrib import admin
from .models import Images


# Register your models here.
class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'price',
        'rating',
        'uploaded_by',
    )


admin.site.register(Images, ImagesAdmin)
