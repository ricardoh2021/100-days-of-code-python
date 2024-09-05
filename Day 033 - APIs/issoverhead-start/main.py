import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = 39.849532  # Your latitude
MY_LONG = -77.174635  # Your longitude
MY_EMAIL = "throwawaylolbob68@gmail.com"
PASSWORD = "wsclpewlnwdafeyf"
CHECK_INTERVAL = 60  # Time between checks in seconds

# API URLs
ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUN_API_URL = "https://api.sunrise-sunset.org/json"

def get_iss_position():
    """Fetches the current position of the ISS from the API."""
    response = requests.get(url=ISS_API_URL)
    response.raise_for_status()
    data = response.json()
    return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])

def is_iss_overhead(iss_latitude, iss_longitude):
    """Checks if the ISS is within 5 degrees of your location."""
    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

def get_sun_times():
    """Fetches the current sunrise and sunset times for your location."""
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get(SUN_API_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset

def is_nighttime(sunrise, sunset):
    """Checks if the current time is after sunset or before sunrise."""
    current_hour = datetime.now().hour
    return current_hour < sunrise or current_hour > sunset

def send_email(subject, body, to_email):
    """Sends an email notification."""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:{subject}\n\n{body}")

def check_iss_and_notify():
    """Checks if the ISS is overhead and sends a notification if conditions are met."""
    iss_latitude, iss_longitude = get_iss_position()
    sunrise, sunset = get_sun_times()

    if is_iss_overhead(iss_latitude, iss_longitude) and is_nighttime(sunrise, sunset):
        send_email("ISS is flying overhead!", "Check outside to see the ISS fly by!", "ceket38100@gmail.com")
        print("Notification sent: ISS is close")
    else:
        print("ISS not close or not nighttime.")

def main():
    """Main loop to continuously check ISS position."""
    start_time = time.monotonic()
    while True:
        check_iss_and_notify()
        time.sleep(CHECK_INTERVAL - ((time.monotonic() - start_time) % CHECK_INTERVAL))

if __name__ == "__main__":
    main()