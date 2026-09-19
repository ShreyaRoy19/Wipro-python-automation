Feature: API Automation using Behave

  Scenario: Fetch user details via GET request
    Given the API endpoint is available
    When I send a GET request to the API
    Then the response status code should be 200