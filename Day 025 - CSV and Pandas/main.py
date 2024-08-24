# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     counter = 0
#     for row in data:
#         if counter > 0:
#             temp = row[1]
#             temperatures.append(int(temp))
#         counter += 1
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# print(temp_list)
#
# max_temp = data.temp.max()
#
# print(max_temp)
# print(data.day)
#
# # Get data in row
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
#
# monday_temp_fahrenheit = monday.temp[0] * 9/5 + 32
#
# print(monday_temp_fahrenheit)


# Create dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "John", "James"],
#     "scores": [10, 9, 10]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240823.csv")

# Replace the fur colors
data["Primary Fur Color"] = data["Primary Fur Color"].replace({
    "Gray": "grey",
    "Cinnamon": "red",
    "Black": "black"
})

# Rename the column
data = data.rename(columns={"Primary Fur Color": "Fur Color"})

# Get the counts of each fur color
fur_color_count = data["Fur Color"].value_counts()

# Print the fur color counts
print(fur_color_count)

# Save the fur color counts to a CSV file with indices
fur_color_count.to_csv("squirrel_count.csv", index=True)