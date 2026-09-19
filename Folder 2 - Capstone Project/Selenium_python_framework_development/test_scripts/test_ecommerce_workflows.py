import pytest
from source_pages.login_screen import LoginScreen
from source_pages.search_screen import SearchScreen
from utils.csv_helper import load_csv_data

test_data_list = load_csv_data("test_inputs.csv")


@pytest.mark.usefixtures("browser_setup")
class TestECommerceWorkflows:

    @pytest.mark.parametrize("data", test_data_list)
    def test_login_and_product_search(self, data):
        login_page = LoginScreen(self.driver)
        login_page.perform_login(data["email"], data["password"])

        assert "My Account" in self.driver.title, f"Authentication failed for user: {data['email']}"

        search_page = SearchScreen(self.driver)
        search_page.search_for_product(data["search_keyword"])

        assert search_page.is_product_displayed(), f"Target product '{data['search_keyword']}' could not be located."