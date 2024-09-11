import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
lat = 39.8309
long = -77.2311
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
ACCOUNT_SID = "ACOUNT_SID"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
client = Client(ACCOUNT_SID, AUTH_TOKEN)
weather_params = {
    "lat": lat,
    "lon": long,
    "appid": API_KEY,
    "cnt": 4
}


def check_weather():
    req = requests.get(url=OWM_ENDPOINT, params=weather_params)
    req.raise_for_status()
    weather_data = req.json()

    weather_list = weather_data["list"]
    #
    # print(req.status_code)
    # print(weather_data)
    # print(weather_list)
    will_rain = False
    for weather_block in weather_list:
        weather = weather_block["weather"]
        weather_id = weather[0]["id"]
        if weather_id < 700:
            will_rain = True
    if will_rain:
        message = client.messages.create(
            from_="whatsapp:+twilio_number",
            body="Bring an Umbrella.😣☂️",
            to="whatsapp:+your_number",

        )

        print(message.status)
    else:
        print("Not going to rain")


check_weather()
