from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from cars.models import Car, Rate


class CarListTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_should_display_car_list(self) -> None:
        car1 = Car.objects.create(make_name="TESLA", model_name="Model S")
        car2 = Car.objects.create(make_name="Honda", model_name="Accord")

        response = self.client.get(reverse('cars'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

        ids = [result['id'] for result in response.json()]
        self.assertTrue(car1.id in ids)
        self.assertTrue(car2.id in ids)

    def test_should_display_correct_average_rate(self) -> None:
        car1 = Car.objects.create(make_name="TESLA", model_name="Model S")
        car2 = Car.objects.create(make_name="Honda", model_name="Accord")
        car3 = Car.objects.create(make_name="Audi", model_name="A3")

        Rate.objects.bulk_create([
            Rate(car=car1, value=5),
            Rate(car=car1, value=5),
            Rate(car=car1, value=2),
            Rate(car=car2, value=2),
        ])

        response = self.client.get(reverse('cars'))
        results = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)

        expected_results = {
            car1.id: 4,
            car2.id: 2,
            car3.id: None
        }

        for result in results:
            self.assertEqual(result['avg_rate'], expected_results[result['id']])
