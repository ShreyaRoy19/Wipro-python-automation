from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# PAGE CLASS FOR ASSIGNMENT 1 
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@id='login-button']")

    def navigate(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_current_url(self):
        return self.driver.current_url


# PAGE CLASS FOR ASSIGNMENT 2 
class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.start_button = (By.XPATH, "//div[@id='start']/button")
        self.finish_text = (By.ID, "finish")

    def navigate(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def click_start(self):
        self.driver.find_element(*self.start_button).click()

    def wait_and_get_hidden_text(self):
        wait = WebDriverWait(self.driver, 5)
        dynamic_element = wait.until(
            EC.visibility_of_element_located(self.finish_text)
        )
        return dynamic_element.text
