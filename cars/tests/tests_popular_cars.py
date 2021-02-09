from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car, Rate


class PopularCarsTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_display_popular_car_list(self) -> None:
        car1 = Car.objects.create(make_name="TESLA", model_name="Model S")
        car2 = Car.objects.create(make_name="Honda", model_name="Accord")
        car3 = Car.objects.create(make_name="Audi", model_name="A3")

        Rate.objects.create(car=car2, value=1)
        Rate.objects.create(car=car2, value=1)
        Rate.objects.create(car=car2, value=1)
        Rate.objects.create(car=car3, value=5)

        response = self.client.get(reverse('popular'))
        results = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #  Expected order car2, car3, car
        self.assertEqual(results[0]["id"], car2.id)
        self.assertEqual(results[1]["id"], car3.id)
        self.assertEqual(results[2]["id"], car1.id)
