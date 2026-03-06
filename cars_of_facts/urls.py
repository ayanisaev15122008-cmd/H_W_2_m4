from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cars_view, name='car_list'),
    path('car/<int:id>/', views.car_detail_view, name='car_detail'),
]