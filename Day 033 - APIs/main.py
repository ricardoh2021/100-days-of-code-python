import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
#
# data_pos = response.json()["iss_position"]
#
# long = data_pos["longitude"]
# lat = data_pos["latitude"]
#
# print(long, lat)

SUNSET_API_URL = "https://api.sunrise-sunset.org/json"
MY_LAT  = 39.849532
MY_LONG = -77.174635
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid" : "America/New_York"
}

res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(res.url)
data = res.json()["results"]

sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)

time_now = datetime.now()

print(time_now)