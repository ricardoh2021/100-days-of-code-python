class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price="N/A", origin_airport="N/A", destination_airport="N/A", out_date="N/A", return_date="N/A"):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def __str__(self):
        return (f"Flight Data:\n"
                f"Price: {self.price}\n"
                f"Origin: {self.origin_airport}\n"
                f"Destination: {self.destination_airport}\n"
                f"Departure Date: {self.out_date}\n"
                f"Return Date: {self.return_date}")

    def _extract_flight_info(self, flight):
        """Extract relevant flight information."""
        return {
            'price': float(flight['price']['total']),
            'origin_airport': flight['itineraries'][0]["segments"][0]["departure"]["iataCode"],
            'destination_airport': flight['itineraries'][0]["segments"][0]["arrival"]["iataCode"],
            'out_date': flight['itineraries'][0]["segments"][0]["departure"]["at"].split("T")[0],
            'return_date': flight['itineraries'][1]["segments"][0]["arrival"]["at"].split("T")[0],
        }

    def find_cheapest_flight(self, json: dict):
        """Find and update the cheapest flight data from the JSON response."""
        meta = json.get('meta', {})
        if meta.get('count', 0) > 0:
            flight_data = json.get('data', [])
            cheapest_flight = min(flight_data, key=lambda x: float(x['price']['total']))
            flight_info = self._extract_flight_info(cheapest_flight)

            self.price = flight_info['price']
            self.origin_airport = flight_info['origin_airport']
            self.destination_airport = flight_info['destination_airport']
            self.out_date = flight_info['out_date']
            self.return_date = flight_info['return_date']