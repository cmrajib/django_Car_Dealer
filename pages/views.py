from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.


# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

# Search Fields
    model_search = Car.objects.values('model').distinct()
    city_search = Car.objects.values('city').distinct()
    year_search = Car.objects.values('year').distinct()
    body_style_search = Car.objects.values('body_style').distinct()


    context = {
    'teams': teams,
    'featured_cars': featured_cars,
    'all_cars': all_cars,
    'model_search': model_search,
    'city_search': city_search,
    'year_search': year_search,
    'body_style_search': body_style_search
    }
    return render(request, 'pages/home.html', context)

def about(request):
    teams = Team.objects.all()
    context = {
    'teams': teams
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})