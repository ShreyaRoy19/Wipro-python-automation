Feature: Page Object Model Login Automation

  Scenario: Successful login using Page Object Model
    Given I open the login web page
    When I provide valid credentials "tomsmith" and "SuperSecretPassword!"
    Then I should see the secure area confirmation message