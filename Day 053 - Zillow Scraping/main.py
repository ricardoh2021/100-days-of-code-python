from time import sleep

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By


def fetch_page(url):
    """Fetch the page content from the given URL."""
    response = requests.get(url)
    return response.text


def clean_price(price_text):
    """Clean and format the price string."""
    match = re.search(r'\$(\d{1,3}(?:,\d{3})*)', price_text)
    return match.group(0) if match else "N/A"  # Return formatted price or N/A


def clean_address(address_text):
    """Clean and format the address string."""
    return ' '.join(address_text.replace('\n', '').replace('|', '').split()).strip()


def parse_listings(html):
    """Parse the HTML content and return a list of dictionaries with address, price, and link."""
    soup = BeautifulSoup(html, "html.parser")
    listings = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    listing_data = []

    for listing in listings:
        link_tag = listing.find(name="a")
        link = link_tag.get("href")

        price_tag = listing.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        price_text = price_tag.get_text().strip() if price_tag else "N/A"  # Handle missing price

        address_tag = listing.find(name="address")
        address_text = address_tag.get_text().strip() if address_tag else "N/A"  # Handle missing address

        # Create a dictionary for each listing
        listing_data.append({
            'link': link,
            'price': clean_price(price_text),
            'address': clean_address(address_text)
        })

    return listing_data
def open_selenium(listings):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSevMHhKyQnU43hz7ri7oYfGFSBA89pzp6v-mlJto8o7jxsTfg/viewform")

    sleep(2)

    for listing in listings:
        fill_form(driver, listing)
        sleep(0.5)
        submit_form(driver)

    driver.quit()

def fill_form(driver, listing):
    """Fill in the Google Form with listing details."""
    address_input = driver.find_element(By.XPATH,
                                        value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_input.send_keys(listing["address"])

    price_input = driver.find_element(By.XPATH,
                                      value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input.send_keys(listing["price"])

    link_input = driver.find_element(By.XPATH,
                                     value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input.send_keys(listing["link"])

    sleep(1)  # Allow for any processing


def submit_form(driver):
    """Submit the Google Form."""
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    sleep(1)  # Wait for the submission to process
    driver.refresh()  # Refresh the page to clear the form for the next entry


def main():
    url = "https://appbrewery.github.io/Zillow-Clone/"

    # Fetch and parse the page
    html_content = fetch_page(url)
    listings = parse_listings(html_content)

    # Display the listing data
    for listing in listings:
        print(listing)

    open_selenium(listings)


if __name__ == "__main__":
    main()