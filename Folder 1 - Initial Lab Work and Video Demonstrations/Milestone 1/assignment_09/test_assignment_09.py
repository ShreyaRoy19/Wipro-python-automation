import json
import pytest
from selenium.webdriver.common.by import By

def load_test_data():
    with open("test_data.json", "r") as file:
        return json.load(file)


@pytest.mark.parametrize("data", load_test_data())
def test_login_scenarios(driver, data):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(data["username"])
    driver.find_element(By.ID, "password").send_keys(data["password"])
    driver.find_element(By.ID, "login-button").click()
    
    if data["expected_error"] is not None:
        actual_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert actual_error == data["expected_error"]
    else:
        actual_title = driver.find_element(By.CLASS_NAME, "title").text
        assert actual_title == "Products"

def test_intentional_failure_for_screenshot(driver):
    """This test is designed to fail so you can see the screenshot in the report."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    actual_title = driver.find_element(By.CLASS_NAME, "title").text
    
    assert actual_title == "Wrong Title", "Triggering a failure for the HTML report screenshot!"
