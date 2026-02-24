from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name = 'car_list'),
    path('create/', views.create_listing, name = 'create_listing'),
    path('<int:car_id>/edit/', views.edit_listing, name = 'edit_listing'),
    path('<int:car_id>/delete/', views.delete_listing, name = 'delete_listing'),
    path('register/', views.register, name = 'register'),
]
