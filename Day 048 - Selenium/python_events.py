from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B00FLYWNYQ/ref=sr_1_2?crid=21D0DB9UUKKS&dib=eyJ2IjoiMSJ9.g1Lrz7oNcd8sVDvjEfcK4woQFm3qlOqvoway1SDbaoXYWSa1I-vHtWfvRVYaNltkDIpU0GG2iuCnBJ9mWPNh5o38DNaE5R-fOevNSH7uuzubRMPB6O3FOZXu1mSu_iE0VXcPDHvTd86ma-F-XDF06NWNGOaUBCihUYnM1GklN0XiFyyZ9-YyOPIdzU0uvmngoa75bd6jLh_AbTPlUtbnn1V2kXIGhz9xSIq7N1CHtHM.L_P3gmZqdTkkK_Fmy488617DC1iQuoqqkcH7srxT6_U&dib_tag=se&keywords=instant%2Bpot&qid=1729021786&sprefix=instant%2Bpot%2B%2Caps%2C154&sr=8-2&th=1")
driver.get("https://www.python.org/")

events_dict = {}

event_widget = driver.find_element(By.CLASS_NAME, value="event-widget")
print(event_widget)

events = event_widget.find_elements(By.TAG_NAME, value="li")
index = 0
for event in events:
    event_info = event.text
    split_text = event_info.split("\n")
    print(event_info)
    if split_text:
        event_value = {"time": split_text[0], "name": split_text[1]}
        events_dict[index] = event_value
    index += 1

print(events_dict)

driver.quit()