from django.shortcuts import render, get_object_or_404
from .models import Car, Brand

def all_cars_view(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    return render(request, 'car_list.html', {'cars': cars, 'brands': brands})

def car_detail_view(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {'car': car})