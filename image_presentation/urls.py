from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_images, name='all_images'),
    path('<int:image_id>/', views.image_view, name='image_view'),
    path('add/', views.add_image, name='add_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
