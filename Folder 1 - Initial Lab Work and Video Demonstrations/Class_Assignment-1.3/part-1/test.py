
# Assignment 1: Web Element Identification -> Identify and locate different web elements on a given webpage 
# using By.ID, By.NAME, By.TAG_NAME, By.LINK_TEXT, and By.CLASS_NAME.
# Example: Locate the username field by ID, password field by Name, and a link by Link Text.


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try: 
    driver.get("http://127.0.0.1:5500/assignment/")

    # 1. Locate username using ID
    username = driver.find_element(By.ID, "username")
    print("Username found:", username.is_displayed())

    # 2. Locate password using NAME
    password = driver.find_element(By.NAME, "password")
    print("Password found:", password.is_displayed())

    # 3. Locate an element using TAG_NAME
    email = driver.find_element(By.TAG_NAME, "input")
    print("Input element found:", email.is_displayed())

    # 4. Locate link using LINK_TEXT
    google_link = driver.find_element(By.LINK_TEXT, "Go to Google")
    print("Google link found:", google_link.is_displayed())

    # 5. Locate button using CLASS_NAME
    login_button = driver.find_element(By.CLASS_NAME, "login-button")
    print("Login button found:", login_button.is_displayed())

except Exception as e:
    print("An error occured")
    print(e)
finally:
    driver.quit()
