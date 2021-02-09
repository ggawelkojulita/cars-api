from django.db.models import Count
from rest_framework import generics

from cars.models import Car, Rate
from cars.serializers import CarSerializer, RateSerializer


class CarsListCreateView(generics.ListCreateAPIView):
    """
        Fetch all existing cars or create the Car instance
        - - - - - - - - - -
        Expected URL format: ((API_URL))/cars
        Method: GET

        Expected response:
        [
            {
                "make_name": "TESLA",
                "model_name": "Model S"
            },
            {
                ...
            }
            ...
        ]

        - - - - - - - - - -
        Expected URL format: ((API_URL))/cars
        Method: POST
        Data: {
            "make_name": "((String))",
            "model_name": "((String))",
        }
    """
    model = Car
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RateCreateView(generics.CreateAPIView):
    """
        Create the Car instance
        - - - - - - - - - -
        Expected URL format: ((API_URL))/cars
        Method: POST
        Data: {
            "make_name": "((String))",
            "model_name": "((String))",
        }
    """
    model = Rate
    serializer_class = RateSerializer


class PopularListView(generics.ListAPIView):
    """
        Top cars ranking based on number of rates
        - - - - - - - - - -
        Expected URL format: ((API_URL))/popular
        Method: GET

        Expected response:
        [
            {
                "make_name": "TESLA",
                "model_name": "Model S"
            },
            {
                ...
            }
            ...
        ]
    """
    model = Car
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all().annotate(rate_count=Count('rate')).order_by('-rate_count')
