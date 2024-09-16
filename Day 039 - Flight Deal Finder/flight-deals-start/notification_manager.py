class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def check_for_notification(self, flights, destinations):
        count = 0
        for dest in destinations["prices"]:
            if flights[count].price < dest["lowestPrice"]:
                print("Price is cheaper")
            else:
                print("Price is not cheaper than in spreadsheet")
            count += 1
