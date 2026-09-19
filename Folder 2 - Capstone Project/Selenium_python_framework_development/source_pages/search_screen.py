from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from source_pages.base_actions import BaseActions

class SearchScreen(BaseActions):
    _SEARCH_INPUT = (By.NAME, "search")
    _SEARCH_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-default')]")
    _PRODUCT_RESULT = (By.XPATH, "//div[@class='product-thumb']")

    def __init__(self, driver_instance):
        super().__init__(driver_instance)

    def search_for_product(self, product_name):
        self.type_text(self._SEARCH_INPUT, product_name)
        self.click_element(self._SEARCH_BUTTON)

    def is_product_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._PRODUCT_RESULT))
            return True
        except:
            return False