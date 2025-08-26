import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

EMAIL_USER = os.getenv("SMTP_EMAIL")
EMAIL_PASS = os.getenv("SMTP_EMAIL_PASSWORD")
APP_PASSWORD = "wscl pewl nwda feyf"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if day_of_week == 2: #Meaning Wednesday
    print("It is Wednesday! Send an email!")
    with open(file="quotes.txt", mode="r") as quotes:
        lines = [line.rstrip('\n') for line in quotes]
    motivational_quote = random.choice(lines)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_USER, to_addrs="ceket38100@gmail.com", msg="Subject:Wednesday "
                                                                                     "Email\n\nEnjoy this week's "
                                                                                     "Motivational Quote!\n"f"{motivational_quote}"
                                                                                      )