class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        """
        Constructor for initializing a new flight data instance with specific travel details.

        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    def __str__(self):
        return (f"Flight Data:\n"
                f"Price: {self.price}\n"
                f"Origin: {self.origin_airport}\n"
                f"Destination: {self.destination_airport}\n"
                f"Departure Date: {self.out_date}\n"
                f"Return Date: {self.return_date}\n"
                f"Stops: {self.stops}")

def find_cheapest_flight(data, is_direct=True):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.

    Args:
        data (dict): The JSON data containing flight information returned by the API.
        is_direct (bool): Flags True if direct flight, False otherwise

    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.

    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
     FlightData object with the details of the most affordable flight.
    """

    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        #Check for flightSearches but with is_direct being false
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", stops="N/A")

    first_flight = data['data'][0]
    stops = 0

    # Data from the first flight in the json
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0 if is_direct else -1]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    stops = len(first_flight["itineraries"][0]["segments"]) - 1 if not is_direct else 0
    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        stops = 0
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            stops = len(first_flight["itineraries"][0]["segments"]) - 1 if not is_direct else 0
            destination = first_flight["itineraries"][0]["segments"][0 if is_direct else -1]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)
            stops = len(first_flight["itineraries"][0]["segments"]) - 1 if not is_direct else 0

            print(f"Lowest price to {destination} is ${lowest_price}")

    return cheapest_flight

