import requests
from behave import given, when, then

@given('the API endpoint is available')
def step_given_endpoint(context):
    context.url = "https://jsonplaceholder.typicode.com/posts/1"

@when('I send a GET request to the API')
def step_when_send_request(context):
    context.response = requests.get(context.url)

@then('the response status code should be {status_code:d}')
def step_then_verify_status(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"
    print(f"API Response Body: {context.response.json()}")