from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import requests
import os
from dotenv import load_dotenv
import logging
from flight_data import FlightData

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        """
        Initializes the FlightSearch class, sets API credentials, and generates an auth token.
        """
        self.AMADEUS_BASE_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.DEPARTURE_AIRPORT = "WAS"
        self.ADULTS = 1
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.six_months_later = (datetime.now() + relativedelta(months=6)).strftime("%Y-%m-%d")
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.cheapest_flights = []

        if not self.api_key or not self.api_secret:
            logging.error("Amadeus API Key or Secret not found in environment variables.")
            raise EnvironmentError("API credentials missing.")

        self.token = self._get_new_token()

    def _get_new_token(self):
        """
        Generates a new authentication token from the Amadeus API.
        """
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }

        try:
            response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
            response.raise_for_status()
            token_data = response.json()
            logging.info(
                f"Token generated: {token_data['access_token']}, expires in {token_data['expires_in']} seconds")
            return token_data['access_token']
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch token: {e}")
            raise

    def get_flight_offers(self, destination_codes: list):
        """
        Retrieves flight offers for the next 6 months for a list of destination airport codes.

        Args:
            destination_codes (list): List of destination IATA codes.
        """
        headers = {"Authorization": f'Bearer {self.token}'}

        for city_code in destination_codes:
            flight_data = FlightData()
            search_params = self._create_search_params(city_code)

            try:
                response = requests.get(url=self.AMADEUS_BASE_URL, params=search_params, headers=headers)
                response.raise_for_status()
                json_response = response.json()
                logging.info(f"API call to {response.url}")
                flight_data.find_cheapest_flight(json_response)
                self.cheapest_flights.append(flight_data)
                logging.info(f"Cheapest flight: {flight_data}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to fetch flight offers for {city_code}: {e}")
        return self.cheapest_flights

    def _create_search_params(self, destination_code):
        """
        Creates the search parameters for the flight offer API call.

        Args:
            destination_code (str): IATA code of the destination airport.

        Returns:
            dict: Dictionary of search parameters for the API request.
        """
        return {
            "originLocationCode": self.DEPARTURE_AIRPORT,
            "destinationLocationCode": destination_code,
            "departureDate": self.tomorrow,
            "returnDate": self.six_months_later,
            "adults": self.ADULTS,
            "nonStop": "true",
            "currencyCode": "USD",
        }