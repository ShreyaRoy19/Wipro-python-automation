from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Task 1: Accept the first alert

driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
time.sleep(1) 
alert.accept()

# Task 2: Dismiss the confirm box 
driver.find_element(By.ID, "confirmbtn").click()

confirm = driver.switch_to.alert
time.sleep(1) # Pause to see the confirm box
confirm.dismiss()

# Task 3: Input text into the prompt and submit
# Since this page lacks a Prompt button, we inject JavaScript to trigger one
driver.execute_script("window.prompt('Please enter some text:', '');")

prompt = driver.switch_to.alert
time.sleep(1) 
prompt.send_keys("Automated Test Data")
prompt.accept()

# Close browser
time.sleep(2)
driver.quit()