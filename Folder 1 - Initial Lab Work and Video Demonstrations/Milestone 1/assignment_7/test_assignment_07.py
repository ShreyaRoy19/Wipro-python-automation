from selenium import webdriver
from pages import LoginPage, DynamicLoadingPage
import time

def run_all_tier1_tests():
    print("Launching browser...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
       
        print("\n--- Running Restructured Assignment 1 ---")
        login_page = LoginPage(driver)
        
        login_page.navigate()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        # Validation for Assignment 1
        actual_url = login_page.get_current_url()
        assert "/inventory.html" in actual_url, "Login failed or URL mismatch!"
        print("Assignment 1 Passed!")
        
        time.sleep(2) 

        
        print("\n--- Running Restructured Assignment 2 ---")
        dynamic_page = DynamicLoadingPage(driver)
        
        dynamic_page.navigate()
        dynamic_page.click_start()
        
        # Validation for Assignment 2
        actual_text = dynamic_page.wait_and_get_hidden_text()
        assert actual_text == "Hello World!", f"Expected 'Hello World!', got '{actual_text}'"
        print("Assignment 2 Passed!")
        
        print("\nSUCCESS: All Tier 1 scripts successfully restructured into POM for Assignment 7!")

    finally:
        print("\nClosing browser...")
        driver.quit()

if __name__ == "__main__":
    run_all_tier1_tests()
