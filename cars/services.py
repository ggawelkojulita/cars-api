import requests

from api.exceptions import VehiclesAPIException

VEHICLE_API_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles'


class VehiclesAPIService:
    @staticmethod
    def get_models(make_name: str):
        """
            Get models by make name
        """
        url = f"{VEHICLE_API_URL}/getmodelsformake/{make_name}/?format=json"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['Results']

        raise VehiclesAPIException()

    @staticmethod
    def get_makes() -> list:
        """
            Get all makes
        """
        url = f"{VEHICLE_API_URL}/getallmakes/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()['Results']

        raise VehiclesAPIException()


class VehiclesService:
    @staticmethod
    def is_correct_model_name(make_name: str, model_name: str) -> bool:
        """
            Check if provided model name is correct
        """
        models = VehiclesAPIService.get_models(make_name)

        filtered_models = list(filter(lambda model: model['Model_Name'] == model_name, models))

        return bool(len(filtered_models))

    @staticmethod
    def is_correct_make_name(make_name: str) -> bool:
        """
            Check if provided make name is correct
        """
        makes = VehiclesAPIService.get_makes()

        filtered_makes = list(filter(lambda model: model['Make_Name'] == make_name, makes))
        return bool(len(filtered_makes))
