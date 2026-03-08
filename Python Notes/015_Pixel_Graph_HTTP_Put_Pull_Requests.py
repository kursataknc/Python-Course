import requests
from datetime import datetime

USERNAME = "kerry"
TOKEN = "12khl4jedh1"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

''' Create a user account '''
user_params = {
	"token": "12khl4jedh1",
	"username": "kerry",
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

''' Create a graph '''
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
	"id": GRAPH_ID,
	"name": "Coding Graph",
	"unit": "min",
	"type": "float",
	"color": "ajisai",
	"timezone": "Etc/GMT+3",
}
headers = {
	"X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

''' Add a pixel to the graph '''
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
yesterday = datetime(year=2022, month=9, day=21).strftime("%Y%m%d")
pixel_data = {
	"date": today,
	"quantity": input("How many minutes did you code today? "),
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


''' Update a pixel '''
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
new_pixel_data = {
	"date": today,
	"quantity": "120",
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


''' Delete a pixel '''
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
