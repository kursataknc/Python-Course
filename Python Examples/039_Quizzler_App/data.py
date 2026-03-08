import requests

parameters = {
	"amount": 10,
	"type": "boolean",
}

respond = requests.get(url="https://opentdb.com/api.php", params=parameters)
respond.raise_for_status()
data = respond.json()
question_data = data["results"]
