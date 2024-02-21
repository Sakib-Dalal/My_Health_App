import requests
from datetime import datetime

PIXELA_NAME = "sakib5001"
PIXELA_TOKEN = "dn350013efe33454fde"

today = datetime.now().date().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_NAME}/graphs/calo1/{today}"

header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.delete(url=graph_endpoint, headers=header)
response.raise_for_status()
print(response.text)

#  https://pixe.la/@sakib5001
