from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B00FLYWNYQ/ref=sr_1_2?crid=21D0DB9UUKKS&dib=eyJ2IjoiMSJ9.g1Lrz7oNcd8sVDvjEfcK4woQFm3qlOqvoway1SDbaoXYWSa1I-vHtWfvRVYaNltkDIpU0GG2iuCnBJ9mWPNh5o38DNaE5R-fOevNSH7uuzubRMPB6O3FOZXu1mSu_iE0VXcPDHvTd86ma-F-XDF06NWNGOaUBCihUYnM1GklN0XiFyyZ9-YyOPIdzU0uvmngoa75bd6jLh_AbTPlUtbnn1V2kXIGhz9xSIq7N1CHtHM.L_P3gmZqdTkkK_Fmy488617DC1iQuoqqkcH7srxT6_U&dib_tag=se&keywords=instant%2Bpot&qid=1729021786&sprefix=instant%2Bpot%2B%2Caps%2C154&sr=8-2&th=1")
driver.get("https://www.python.org/")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is ${price_dollar}.{price_cents}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link)

link = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[3]/p[2]/a')
print(link.get_attribute("href"))

driver.quit()