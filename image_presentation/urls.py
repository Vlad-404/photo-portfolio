from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_images, name='all_images'),
    path('image_view/', views.image_view, name='image_view'),
]
