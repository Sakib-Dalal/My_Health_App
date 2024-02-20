import requests
from datetime import datetime


class SheetData:
    def __init__(self):
        self.sheet_response = None
        self.h_data = None
        self.sheety_endpoint = "https://api.sheety.co/822d50c0ba48a0d28feb2305a5a52d6c/workoutTracking/workouts"
        self.today = datetime.now().date().strftime("%d/%m/%Y")
        self.time = datetime.now().time().strftime("%X")

    def send_data_to_sheet(self, health_data):
        self.h_data = health_data["exercises"]
        for data in self.h_data:
            sheet_input = {
                "workout": {
                    "date": self.today,
                    "time": self.time,
                    "exercise": data["name"],
                    "duration": data["duration_min"],
                    "calories": data["nf_calories"]
                }
            }
            self.sheet_response = requests.post(url=self.sheety_endpoint, json=sheet_input)
            print(self.sheet_response.text)
            print("Data 📊 Added Successfully")
