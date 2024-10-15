import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_chrome_driver():
    """Initialize and return a Chrome WebDriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=chrome_options)


def click_cookie(driver, cookie_element):
    """Click the cookie repeatedly."""
    cookie_element.click()


def get_cookie_count(driver):
    """Retrieve the current number of cookies."""
    cookie_count = driver.find_element(By.ID, "money").text
    return int(cookie_count.replace(",", ""))


def get_upgrades(driver, cps_gain_map):
    """Get a list of upgrades with their CPS gain and cost."""
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
    upgrade_info = []
    for upgrade in upgrades:
        if upgrade.text:
            name_price = upgrade.text.split(" - ")
            if len(name_price) == 2:
                name, price = name_price
                price = int(price.replace(",", ""))
                cps_gain = cps_gain_map.get(name, 0)  # Get the CPS gain for the upgrade
                if cps_gain > 0:  # Ensure CPS gain data is available
                    cost_benefit_ratio = cps_gain / price
                    upgrade_info.append((name, price, cps_gain, cost_benefit_ratio, upgrade))
    return sorted(upgrade_info, key=lambda x: x[3], reverse=True)

def purchase_upgrade(driver, cookie_count, cps_gain_map):
    """Purchase the upgrade with the best cost-to-benefit ratio."""
    upgrade_info = get_upgrades(driver, cps_gain_map)
    for name, price, cps_gain, ratio, element in upgrade_info:
        if cookie_count >= price:
            element.click()
            break

def main():
    # Initialize the WebDriver
    driver = get_chrome_driver()
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    # Get the cookie element
    cookie = driver.find_element(By.ID, "cookie")

    # Time management for 5 minutes (300 seconds)
    start_time = time.time()
    timeout = 300  # 5 minutes in seconds
    upgrade_interval = 10  # Check for upgrades every 5 seconds

    # Mapping of upgrade names to their CPS gain
    cps_gain_map = {
        "Cursor": 0.1,
        "Grandma": 0.5,
        "Factory": 4,
        "Mine": 10,
        "Shipment": 20,
        "Alchemy lab": 50,
        "Portal": 100,
        "Time machine": 200,
    }

    last_upgrade_time = time.time()

    try:
        # Main loop: Click cookie as fast as possible and buy upgrades
        while time.time() - start_time < timeout:
            click_cookie(driver, cookie)

            # Check for upgrades every upgrade_interval seconds
            if time.time() - last_upgrade_time >= upgrade_interval:
                cookie_count = get_cookie_count(driver)
                purchase_upgrade(driver, cookie_count, cps_gain_map)
                last_upgrade_time = time.time()

        # After 5 minutes, get the cookies per second rate
        cps = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cps}")
    finally:
        # Quit the driver
        driver.quit()


if __name__ == "__main__":
    main()