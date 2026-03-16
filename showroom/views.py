from django.shortcuts import render, get_object_or_404
from .models import Car

def home(request):
    featured_cars = Car.objects.filter(is_featured=True)[:3]
    carousel_cars = Car.objects.all()
    return render(request, 'showroom/home.html', {'featured_cars': featured_cars, 'carousel_cars': carousel_cars})

def catalog(request):
    category = request.GET.get('category')
    cars = Car.objects.all()
    
    if category in ['RENT', 'SALE']:
        cars = cars.filter(category=category)
        
    return render(request, 'showroom/catalog.html', {'cars': cars, 'current_category': category})

def detail(request, slug):
    car = get_object_or_404(Car, slug=slug)
    specs = car.specs  # In a real app, might want to parse JSON if it's stored as such
    return render(request, 'showroom/detail.html', {'car': car, 'specs': specs})

def contacts(request):
    return render(request, 'showroom/contacts.html')
