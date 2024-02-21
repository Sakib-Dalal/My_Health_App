import requests

API_ID = "7a8f2978"
API_KEY = "b76e146773bd5d54afd0b152c2259220"


class AiHealth:
    def __init__(self):
        self.health_data = None
        self.health_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.header = {
            "x-app-id": API_ID,
            "x-app-key": API_KEY
        }

    def get_calories(self):
        string_text = input("Tell me which exercise you did 💪: ")
        parameters = {
            "query": string_text,
            "gender": "male",
            "weight_kg": 75,
            "height_cm": 180,
            "age": 19
        }

        response = requests.post(url=self.health_endpoint, json=parameters, headers=self.header)
        self.health_data = response.json()
        return self.health_data
