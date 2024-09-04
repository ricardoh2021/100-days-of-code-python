import smtplib
import datetime as dt
import random

MY_EMAIL = "throwawaylolbob68@gmail.com"
PASSWORD = "wsclpewlnwdafeyf"
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
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ceket38100@gmail.com", msg="Subject:Wednesday "
                                                                                     "Email\n\nEnjoy this week's "
                                                                                     "Motivational Quote!\n"f"{motivational_quote}"
                                                                                      )