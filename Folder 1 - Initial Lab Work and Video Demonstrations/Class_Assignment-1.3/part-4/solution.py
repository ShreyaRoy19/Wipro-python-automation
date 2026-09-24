from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome
driver = webdriver.Chrome()

try:
    # 1. Load the page
    driver.get("file:///C:/Users/SHREYA/OneDrive/Desktop/python1/assignment.html")
    
    # 2. Locate child node using CSS Selector (div parent > button child)
    css_selector = "div.login-panel > button"
    
    # Wait efficiently until the specific child element is present and clickable
    wait = WebDriverWait(driver, 10)
    child_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    
    # 3. Output the result
    print(f"Success! Found element with text: '{child_button.text}'")
    child_button.click()

finally:
    
    import time
    time.sleep(2)
    driver.quit()
