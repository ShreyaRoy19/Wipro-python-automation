from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@given('I open the login web page')
def step_open_page(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('I provide valid credentials "{username}" and "{password}"')
def step_enter_creds(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()

@then('I should see the secure area confirmation message')
def step_verify_login(context):
    message = context.login_page.get_success_message()
    assert "You logged into a secure area!" in message, unexpected_msg if 'unexpected_msg' in locals() else f"Login failed, got message: {message}"
    context.driver.quit()