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


class CarListTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_display_car_list(self) -> None:
        Car.objects.create(make_name="TESLA", model_name="Model S")
        Car.objects.create(make_name="Honda", model_name="Accord")

        response = self.client.get(reverse('cars'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)


class RateCreationTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_fail_for_not_existing_car(self) -> None:
        data = {
            "car_id": 1,
            "value": 1
        }

        response = self.client.post(reverse('rate'), data)

        self.assertEqual(response.status_code, 400)

    def test_should_fail_for_incorrect_rate(self) -> None:
        car = Car.objects.create(make_name="TESLA", model_name="Model S")

        data = {
            "car": car.pk,
            "value": 6
        }

        response = self.client.post(reverse('rate'), data)
        print(response.json())

        self.assertEqual(response.status_code, 400)

    def test_should_save_rate(self) -> None:
        car = Car.objects.create(make_name="TESLA", model_name="Model S")

        data = {
            "car": car.pk,
            "value": 5
        }

        response = self.client.post(reverse('rate'), data)
        print(response.json())

        self.assertEqual(response.status_code, 201)
