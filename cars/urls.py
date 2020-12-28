from django.urls import path
from . import views

urlpatterns = [
    path('',views.cars, name='cars'),
    path('<int:car_id>/',views.car_details, name='car_details'),
    path('search/',views.search, name='search'),
]
 
