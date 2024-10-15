from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_box = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
first_name_box.send_keys("Ricardo")

last_name_box = driver.find_element(By.NAME, value="lName")
last_name_box.send_keys("Hernandez")

email_address_box = driver.find_element(By.NAME, value="email")
email_address_box.send_keys("testing@gaim.com")

submit_btn = driver.find_element(By.XPATH, value="/html/body/form/button")
submit_btn.click()
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)
# driver.quit()

