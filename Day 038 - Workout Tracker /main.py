import requests
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv()

api_key = os.getenv("NUTRITIONIX_API_KEY")
app_id = os.getenv("NUTRITIONIX_APP_ID")
bearer_token = os.getenv("SHEETY_BEARER_TOKEN")

NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7babb33380db5947af270c730b35b565/myWorkouts/workouts"

weight = 79.3787 #kilos
height= 175.26 #centimers
age = 25


headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

nutritionix_params = {
    "query": str(input("Tell me which exercises you did: ")),
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

# Define the headers for the POST request
sheety_headers = {
    'Authorization': f'Bearer {bearer_token}',  # Bearer token included in Authorization header
    'Content-Type': 'application/json'  # Adjust content-type depending on the API
}



res = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, headers=headers, json=nutritionix_params)

print(res.status_code)
exercises_json = res.json()

# exercises_json = {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 20, 'met': 9.8, 'nf_calories': 228.67, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 766, 'user_input': 'tricep', 'duration_min': 30, 'met': 3.5, 'nf_calories': 122.5, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 2054, 'name': 'weight lifting', 'description': None, 'benefits': None}, {'tag_id': 774, 'user_input': 'workout', 'duration_min': 30, 'met': 4, 'nf_calories': 140, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 2143, 'name': 'General Workout', 'description': None, 'benefits': None}]}

exercises = exercises_json["exercises"]

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in exercises:
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    print(name, duration, calories)
    sheety_params = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(response.status_code)

# print(exercises)


print(current_time)
print(current_date)
