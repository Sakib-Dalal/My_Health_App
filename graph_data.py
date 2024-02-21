import requests
from datetime import datetime

PIXELA_NAME = "sakib5001"
PIXELA_TOKEN = "dn350013efe33454fde"

GRAPH_ID_CALO = "calo1"
GRAPH_ID_TIME = "time1"

PIXELA_ERROR_MESSAGE = "{'message': 'Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter. If you are interested in being a Pixela supporter, please see: https://github.com/a-know/Pixela/wiki/How-to-support-Pixela-by-Patreon-%EF%BC%8F-Use-Limited-Features', 'isSuccess': False, 'isRejected': True}"


class Graphs:
    def __init__(self):
        self.old_pixel = None
        self.pixela_data_old = None
        self.duration_response = None
        self.calories_response = None
        self.calories = None
        self.duration = None
        self.new_duration = None
        self.new_calories = None
        self.graph_para_dura = None
        self.graph_para_calo = None
        self.graph_get_time_endpoint = None
        self.graph_para = None
        self.graph_get_calo_endpoint = None
        self.h_data = None
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_endpoint_calo = f"{self.pixela_endpoint}/{PIXELA_NAME}/graphs/{GRAPH_ID_CALO}"
        self.graph_endpoint_time = f"{self.pixela_endpoint}/{PIXELA_NAME}/graphs/{GRAPH_ID_TIME}"
        self.header = {
            "X-USER-TOKEN": PIXELA_TOKEN
        }
        self.today = datetime.now().date().strftime("%Y%m%d")

    def get_pixel(self):
        self.graph_get_calo_endpoint = f"{self.graph_endpoint_calo}/{self.today}"
        self.graph_get_time_endpoint = f"{self.graph_endpoint_time}/{self.today}"

        self.calories = requests.get(url=self.graph_get_calo_endpoint, headers=self.header)
        self.duration = requests.get(url=self.graph_get_time_endpoint, headers=self.header)

        if self.calories.json() == PIXELA_ERROR_MESSAGE or self.duration.json() == PIXELA_ERROR_MESSAGE:
            self.get_pixel()
        else:
            try:
                self.pixela_data_old = {"calories": self.calories.json()['quantity'],
                                        "duration": self.duration.json()['quantity']}
            except:
                self.get_pixel()
            return self.pixela_data_old

    def send_graph_data(self, health_data):
        self.h_data = health_data['exercises']
        self.old_pixel = self.get_pixel()
        print("✅ Old pixel data received")

        for data in self.h_data:
            self.new_calories = float(self.old_pixel['calories']) + float(data['nf_calories'])
            self.new_duration = int(self.old_pixel['duration']) + int(data['duration_min'])

            print(f"new data: calories: {self.new_calories}, duration: {self.new_duration}")
            self.post_response()

    def post_response(self):
        self.graph_para_calo = {
            "date": self.today,
            "quantity": str(self.new_calories)
        }
        self.graph_para_dura = {
            "date": self.today,
            "quantity": str(self.new_duration)
        }

        self.calories_response = requests.post(url=self.graph_endpoint_calo, headers=self.header,
                                               json=self.graph_para_calo)
        self.duration_response = requests.post(url=self.graph_endpoint_time, headers=self.header,
                                               json=self.graph_para_dura)

        if self.calories_response.json()['isSuccess'] != True or self.duration_response.json()['isSuccess'] != True:
            self.post_response()
        else:
            print("✅ Data added Successful")
