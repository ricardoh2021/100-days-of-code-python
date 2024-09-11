import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
import math

# Load environment variables
load_dotenv()

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

# API keys from environment variables
news_api_key = os.getenv("NEWS_API_KEY")
stock_api_key = os.getenv("AA_API_KEY")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("AUTH_TOKEN")

# Twilio client
client = Client(twilio_account_sid, twilio_auth_token)


# Function to fetch stock data
def get_stock_data(stock_symbol):
    stock_params = {
        "function": FUNCTION,
        "symbol": stock_symbol,
        "apikey": stock_api_key
    }
    response = requests.get(url=STOCK_API_URL, params=stock_params)
    response.raise_for_status()
    return response.json()["Time Series (Daily)"]


# Function to fetch news
def get_news(company_name):
    news_params = {
        "apikey": news_api_key,
        "country": "us",
        "q": company_name
    }
    response = requests.get(url=NEWS_API_URL, params=news_params)
    response.raise_for_status()
    return response.json()["articles"][:3]


# Function to calculate percentage change
def calculate_percentage_change(yesterday_close, day_before_yesterday_close):
    change_in_dollars = day_before_yesterday_close - yesterday_close
    percent_change = round((math.fabs(change_in_dollars) / day_before_yesterday_close) * 100, 2)
    return change_in_dollars, percent_change


# Function to check if change exceeds 5%
def exceeds_threshold(percent_change):
    return percent_change >= 5


# Function to send WhatsApp notification
def send_notification(stock_symbol, percent, articles, change_in_dollars):
    direction = "🔺" if change_in_dollars < 0 else "🔻"
    message = f"{stock_symbol}: {direction}{percent}%\n\n"

    for article in articles:
        message += f"Headline: {article['title']}\n"
        message += f"Brief: {article['description']}\n\n"

    print(message)
    text = client.messages.create(
        from_="whatsapp:+twillio_num",
        body=message,
        to="whatsapp:+yourNum",
    )
    print(text.status)


# Main logic
def main():
    # Replace this mock data with the actual API call when necessary
    stock_dates_data = [
        ('2024-09-09', {'1. open': '216.2000', '2. high': '219.8700', '3. low': '213.6700', '4. close': '216.2700',
                        '5. volume': '67443518'}),
        ('2024-09-08', {'1. open': '220.0000', '2. high': '222.0000', '3. low': '215.0000', '4. close': '220.5000',
                        '5. volume': '60000000'})
    ]

    yesterday_close = float(stock_dates_data[0][1]['4. close'])
    day_before_yesterday_close = float(stock_dates_data[1][1]['4. close'])

    change_in_dollars, percent_change = calculate_percentage_change(yesterday_close, day_before_yesterday_close)

    if exceeds_threshold(percent_change):
        print("Get news")
        articles = get_news(COMPANY_NAME)
        send_notification(STOCK, percent_change, articles, change_in_dollars)
    else:
        print(f"The change in percentage was {percent_change}%.")


if __name__ == "__main__":
    main()