import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def run_data_driven_test():
    test_cases = load_test_data("test_data.json")
    
    print("Launching browser...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        for data in test_cases:
            print(f"\nExecuting Scenario: {data['scenario']}")
            
            # Navigate and Login
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys(data["username"])
            driver.find_element(By.ID, "password").send_keys(data["password"])
            driver.find_element(By.ID, "login-button").click()
            
            
            if data["expected_error"] is not None:
                # Assert Incorrect Login (Error Message)
                error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
                actual_error = error_element.text
                assert actual_error == data["expected_error"], f"Failed! Expected '{data['expected_error']}' but got '{actual_error}'"
                print("Assertion Passed: Correct validation error displayed.")
            
            else:
                # Assert Correct Login 
                title_element = driver.find_element(By.CLASS_NAME, "title")
                actual_title = title_element.text
                assert actual_title == "Products", f"Failed! Expected dashboard title 'Products' but got '{actual_title}'"
                print("Assertion Passed: Successfully logged in and reached dashboard.")
            
            time.sleep(1) 

    finally:
        print("\nClosing browser...")
        driver.quit()

if __name__ == "__main__":
    run_data_driven_test()