import requests
from datetime import datetime
response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(f" Current ISS location is: {iss_position}")

parameters = {
	"lat": 37.579609,
	"lng": 36.946812,
	"formatted":0,
}
sunset_loc = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunset_loc.raise_for_status()
sunrise = sunset_loc.json()["results"]["sunrise"]
sunset = sunset_loc.json()["results"]["sunset"]
sunrise = sunrise.split("T")[1].split("+")
sunset = sunset.split("T")[1].split("+")
print(f"{sunrise}\n{sunset}")

time_now = datetime.now()
print(time_now)