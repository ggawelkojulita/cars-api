from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car


class RateCreationTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_fail_for_not_existing_car(self) -> None:
        data = {
            "car_id": 1,
            "value": 1
        }

        response = self.client.post(reverse('rate'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_fail_for_incorrect_rate(self) -> None:
        car = Car.objects.create(make_name="TESLA", model_name="Model S")

        data = {
            "car": car.pk,
            "value": 6
        }

        response = self.client.post(reverse('rate'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_save_rate(self) -> None:
        car = Car.objects.create(make_name="TESLA", model_name="Model S")

        data = {
            "car": car.pk,
            "value": 5
        }

        response = self.client.post(reverse('rate'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
