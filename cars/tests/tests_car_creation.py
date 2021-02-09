from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car


class CarCreationTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_fail_for_not_unique_data(self) -> None:
        Car.objects.create(make_name="TESLA", model_name="Model S")

        data = {
            "make_name": "TESLA",
            "model_name": "Model S"
        }

        response = self.client.post(reverse('cars'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_fail_for_empty_make_name(self) -> None:
        data = {
            "make_name": "TESLA",
        }

        response = self.client.post(reverse('cars'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_fail_for_empty_model_name(self) -> None:
        data = {
            "make_name": "TESLA",
        }

        response = self.client.post(reverse('cars'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_save_car(self)-> None:
        data = {
            "make_name": "HONDA",
            "model_name": "Accord"
        }

        response = self.client.post(reverse('cars'), data)

        self.assertEqual(response.status_code, 201)

    def test_should_fail_for_not_existing_make_name(self)-> None:
        data = {
            "make_name": "XYZ",
            "model_name": "123"
        }

        response = self.client.post(reverse('cars'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
