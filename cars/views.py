from django.shortcuts import render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    featured_cars = Car.objects.order_by('-created_date')
# pagination
    paginator = Paginator(featured_cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # Search Fields
    model_search = Car.objects.values('model').distinct()
    city_search = Car.objects.values('city').distinct()
    year_search = Car.objects.values('year').distinct()
    body_style_search = Car.objects.values('body_style').distinct()
    transmission_search = Car.objects.values('transmission').distinct()

    context = {
        'featured_cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search':year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/cars.html', context)

def car_details(request, car_id):
    car = Car.objects.get(pk=car_id)
    context = {
        'car': car
    }
    return render(request, 'cars/car_details.html', context)

def search(request):
    featured_cars = Car.objects.order_by('-created_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
             featured_cars = featured_cars.filter(description__icontains=keywords)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
             featured_cars = featured_cars.filter(model__iexact=model)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
             featured_cars = featured_cars.filter(city__iexact=city)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
             featured_cars = featured_cars.filter(year__iexact=year)
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
             featured_cars = featured_cars.filter(body_style__iexact=body_style)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
             featured_cars = featured_cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            featured_cars = featured_cars.filter(price__gte=min_price, price__lte=max_price)

# pagination
    paginator = Paginator(featured_cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    return render(request, 'cars/search.html', {'featured_cars': paged_cars})

# ========
# queryset_list = Listing.objects.order_by('-list_date')
#
#
# if 'keywords' in request.GET:
#     keywords = request.GET['keywords']
#     if keywords:
#          queryset_list = queryset_list.filter(description__icontains=keywords)
# # city
# if 'city' in request.GET:
#     city = request.GET['city']
#     if city:
#          queryset_list = queryset_list.filter(city__iexact=city)
#
# # state
# if 'state' in request.GET:
#     state = request.GET['state']
#     if state:
#          queryset_list = queryset_list.filter(state__iexact=state)
#
# # bedrooms
# if 'bedrooms' in request.GET:
#     bedrooms = request.GET['bedrooms']
#     if bedrooms:
#          queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
#
# # price
# if 'price' in request.GET:
#     price = request.GET['price']
#     if price:
#          queryset_list = queryset_list.filter(price__lte=price)
#
#
#
# context = {
#     'price_choices': price_choices,
#     'bedroom_choices': bedroom_choices,
#     'state_choices': state_choices,
#     'listings': queryset_list,
#     'values': request.GET,
# }
# return render(request, 'listings/search.html', context)
