from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
linkedin_job_url = "https://www.linkedin.com/jobs/search/?currentJobId=3910549495&f_AL=true&f_E=2&f_TPR=r2592000&f_WT=2&geoId=103644278&keywords=Software%20Engineer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&spellCorrectionEnabled=true"
linkedin_url = "https://www.linkedin.com/login"

driver.get(linkedin_url)

# Login
input_box = driver.find_element(By.ID, value="username")
password_box = driver.find_element(By.ID, value="password")
input_box.send_keys(os.getenv("LINKEDIN_EMAIL"))
password_box.send_keys(os.getenv("LINKEDIN_PASSWORD"))

login_form_container = driver.find_element(By.CLASS_NAME, value="login__form_action_container")
login_form_container.click()

driver.get(linkedin_job_url)

try:
    job_board = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "scaffold-layout__list-container"))  # This is a dummy element
    )

    jobs = job_board.find_elements(By.CLASS_NAME, value="job-card-container--clickable")

    for job in jobs:
        job.click()
        time.sleep(1)  # Wait for the job details to load

        # Check if "Easy Apply" button is present
        try:
            easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
            if "Easy Apply" in easy_apply_button.text:
                print(f"Applying to: {job.text}")
                easy_apply_button.click()
                # Fill out application as needed
                time.sleep(2)  # Adjust sleep time as necessary for application processing
            else:
                print(f"Skipping (not 1-step): {job.text}")
        except Exception as e:
            print(f"Skipping (no Easy Apply): {job.text}")

finally:
    driver.quit()
# job_info_container = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--container")
#
# easy_apply_btn = job_info_container.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
# easy_apply_btn.click()
#

# sign_in_btn = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/div[2]/a')
# sign_in_btn.click()
