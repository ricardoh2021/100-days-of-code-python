import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7babb33380db5947af270c730b35b565/flightDeals/prices"
SHEETY_USERS_ENDPOINT ="https://api.sheety.co/7babb33380db5947af270c730b35b565/flightDeals/users"

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        # response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        # data = response.json()
        data = [{'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 2}, {'city': 'Barcelona', 'iataCode': 'BCN', 'lowestPrice': 551, 'id': 3}, {'city': 'Mexico City', 'iataCode': 'MEX', 'lowestPrice': 400, 'id': 4}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 800, 'id': 5}, {'city': 'Kathmandu', 'iataCode': 'KTM', 'lowestPrice': 1000, 'id': 6}]
        # self.destination_data = data["prices"]
        self.destination_data = data
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        submissions = response.json()["users"]
        email_list = []
        for entry in submissions:
            email = entry["whatIsYourEmailAddress?"]
            email_list.append(email)
        return email_list