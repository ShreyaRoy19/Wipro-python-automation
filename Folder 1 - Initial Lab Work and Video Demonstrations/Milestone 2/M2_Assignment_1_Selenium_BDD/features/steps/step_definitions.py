from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given('I launch the Chrome browser')
def step_launch_browser(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

@when('I open the Google homepage')
def step_open_url(context):
    context.driver.get("https://www.google.com")

@then('I verify the page title contains Google')
def step_verify_title(context):
    assert "Google" in context.driver.title
    context.driver.quit()