from django.urls import path
from cars.views import CarsListCreateView, RateCreateView

urlpatterns = [
    path('cars', CarsListCreateView.as_view(), name="cars"),
    path('rate', RateCreateView.as_view(), name="rate"),
]
