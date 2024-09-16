import requests
import os
from dotenv import load_dotenv


class DataManager:
    load_dotenv()
    #This class is responsible for talking to the Google Sheet.
    SHEETY_ENDPOINT = "https://api.sheety.co/7babb33380db5947af270c730b35b565/flightDeals/prices"
    bearer_token = os.getenv("SHEETY_BEARER_TOKEN")

    # Define the headers for the POST request
    sheety_headers = {
        'Authorization': f'Bearer {bearer_token}',  # Bearer token included in Authorization header
        'Content-Type': 'application/json'  # Adjust content-type depending on the API
    }

    def __init__(self):
        pass

    def get_data(self):
        res = requests.get(url=self.SHEETY_ENDPOINT, headers=self.sheety_headers)
        data = res.json()
        # print(res.status_code)

        # data = {'prices': [{'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 2},
        #                                {'city': 'Barcelona', 'iataCode': 'BCN', 'lowestPrice': 551, 'id': 3},
        #                                {'city': 'Mexico City', 'iataCode': 'MEX', 'lowestPrice': 400, 'id': 4},
        #                                {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 5}]}

        return data

    def get_destination_codes(self):
        data = self.get_data()

        iata_codes = [item['iataCode'] for item in data['prices']]

        return iata_codes

