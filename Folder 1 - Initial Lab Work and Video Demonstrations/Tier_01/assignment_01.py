from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Initialize WebDriver and navigate to the page
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# 2. Interact using the required locator strategies
# Username using By.ID
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Password using By.NAME
driver.find_element(By.NAME, "password").send_keys("secret_sauce")

# Login Button using By.XPATH
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# 3. Validation: Assert URL contains /inventory.html
assert "/inventory.html" in driver.current_url, "Login failed or URL mismatch!"
print("Assignment 1 successful: Successfully logged in and verified URL.")

driver.quit()