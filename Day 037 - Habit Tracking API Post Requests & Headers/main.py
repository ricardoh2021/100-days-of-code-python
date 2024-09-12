import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}



# ----------------- Create username -----------------#
# res = requests.post(url=pixela_endpoint, json=user_params)
#
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Miles",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


#--------------- Create a Graph -------------------#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#
# print(response.text)

post_single_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

print(today.strftime("%Y%m%d"))

single_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many miles did you run today?")
}
#
res = requests.post(url=post_single_pixel_endpoint, json=single_pixel_params, headers=headers)

print(res.text)

# yesterday_pixel_endpoint = f"{post_single_pixel_endpoint}/20240911"
#
# res = requests.delete(url=yesterday_pixel_endpoint, headers=headers)

