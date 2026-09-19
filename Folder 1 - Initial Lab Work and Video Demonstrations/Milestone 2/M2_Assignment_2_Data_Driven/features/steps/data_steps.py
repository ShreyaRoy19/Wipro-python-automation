from behave import given, when, then

@given('I navigate to the login page')
def step_navigate(context):
    print("Navigating to login page...")

@when('I enter "{username}" and "{password}"')
def step_enter_credentials(context, username, password):
    print(f"Entering User: {username} and Password: {password}")

@then('I validate the login result')
def step_validate(context):
    print("Validating test outcome...")