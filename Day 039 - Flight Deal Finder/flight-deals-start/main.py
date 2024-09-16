#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
text = NotificationManager()


# Create a list of formatted dates for the next 6 months
# dates_6_months = [(today + relativedelta(months=i)).strftime("%Y-%m-%d") for i in range(1, 7)]

# Print the list of dates
# print(dates_6_months)

#Uncomment below line when API is in use. Sample data in the second variable.
destination_data = data_manager.get_data()
print(destination_data)
destination_list = data_manager.get_destination_codes()


cheap_flights_list = flight_search.get_flight_offers(destination_list)

text.check_for_notification(cheap_flights_list, destination_data)




