from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car


class CarListTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_display_car_list(self) -> None:
        Car.objects.create(make_name="TESLA", model_name="Model S")
        Car.objects.create(make_name="Honda", model_name="Accord")

        response = self.client.get(reverse('cars'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)
