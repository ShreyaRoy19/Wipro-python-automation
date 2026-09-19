from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome browser
driver = webdriver.Chrome()

# Task: Navigate to a page with dynamic content 

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Find "Start" button and click it
start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()
 
# Implement WebDriverWait 

wait = WebDriverWait(driver, 5)


dynamic_element = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

# Print the revealed text to verify it worked successfully
print("Text revealed:", dynamic_element.text)

# Close the browser
driver.quit()