import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0"
accept_language = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Dnt": "1",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0",
}

res = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

product_block = soup.find(name="div", class_="a-box-group")
product_title = soup.find(name="span", id="productTitle")

# Extract the text and ensure it is properly encoded to handle non-ASCII characters
product_title = product_title.getText().strip()

# Use split and join to remove extra spaces and line breaks
product_title = " ".join(product_title.split())

print(product_title)



if product_block:
    price_block = product_block.find(name="span", class_="a-offscreen")
    if price_block:
        price = price_block.getText().strip()
        print(price)

        # Properly encode the email body to handle non-ASCII characters
        email_body = f"Subject: Amazon Price Alert!\n\n{product_title} is now {price}!".encode("utf-8")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("SMTP_EMAIL"), password=os.getenv("SMTP_EMAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.getenv("SMTP_EMAIL"),
                to_addrs="ceket38100@gmail.com",
                msg=email_body
            )