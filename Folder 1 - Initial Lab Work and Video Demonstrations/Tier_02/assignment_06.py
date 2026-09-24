from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Store the original window handle
main_layout = driver.current_window_handle

# Task 1: Iframes
print("--- Handling iFrame ---")

driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(10)

driver.switch_to.frame("courses-iframe")

iframe_element = driver.find_element(By.TAG_NAME, "h2")
print(f"Text extracted from inside the iframe: '{iframe_element.text}'")

driver.switch_to.default_content()

# Task 2: Windows and Tabs
print("\n--- Handling New Tabs ---")

driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

driver.find_element(By.ID, "opentab").click()
time.sleep(2)

for window_handle in driver.window_handles:
    if window_handle != main_layout:
        driver.switch_to.window(window_handle)
        break

new_tab_title = driver.title
print(f"The title of the new tab is: '{new_tab_title}'")

driver.close()

driver.switch_to.window(main_layout)
print("Successfully switched back to the main window.")

time.sleep(2)
driver.quit()
