##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


MY_EMAIL = "throwawaylolbob68@gmail.com"
PASSWORD = os.getenv("SMTP_EMAIL_PASSWORD")


letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv
df = pd.read_csv('birthdays.csv')
birthday_dict = df.to_dict()

birthday_names = birthday_dict["name"]
birthday_email = birthday_dict["email"]
birthday_months = birthday_dict["month"]
birthday_days = birthday_dict["day"]

birthdate_combined = {i: (birthday_months[i], birthday_days[i]) for i in birthday_months}


now = dt.datetime.now()
month = now.month
day = now.day
today_date = (month, day)


# 2. Check if today matches a birthday in the birthdays.csv
def check_birthday_today():
    for index in birthdate_combined:
        birthday = birthdate_combined[index]
        if today_date == birthday:
            name = birthday_names.get(index)
            email = birthday_email.get(index)
            letter_file_path = random.choice(letters)

            with open(file=f"letter_templates/{letter_file_path}", mode="r") as file:
                content = file.read()

            personalized_msg = content.replace("[NAME]", name)
            print(personalized_msg)

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{personalized_msg}")


check_birthday_today()
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
