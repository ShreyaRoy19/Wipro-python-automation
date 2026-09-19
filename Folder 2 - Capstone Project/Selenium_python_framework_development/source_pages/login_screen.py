from selenium.webdriver.common.by import By
from source_pages.base_actions import BaseActions

class LoginScreen(BaseActions):
    _MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    _LOGIN_OPTION = (By.LINK_TEXT, "Login")
    _EMAIL_FIELD = (By.ID, "input-email")
    _PASSWORD_FIELD = (By.ID, "input-password")
    _LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")

    def __init__(self, driver_instance):
        super().__init__(driver_instance)

    def perform_login(self, email, password):
        self.click_element(self._MY_ACCOUNT)
        self.click_element(self._LOGIN_OPTION)
        self.type_text(self._EMAIL_FIELD, email)
        self.type_text(self._PASSWORD_FIELD, password)
        self.click_element(self._LOGIN_BUTTON)