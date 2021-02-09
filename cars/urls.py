from django.urls import path
from cars.views import CarsListCreateView, RateCreateView, PopularListView

urlpatterns = [
    path('cars', CarsListCreateView.as_view(), name="cars"),
    path('rate', RateCreateView.as_view(), name="rate"),
    path('popular', PopularListView.as_view(), name="popular"),
]
