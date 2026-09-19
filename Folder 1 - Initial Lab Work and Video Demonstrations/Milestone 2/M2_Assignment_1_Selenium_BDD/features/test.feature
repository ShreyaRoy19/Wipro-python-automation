Feature: Wipro Selenium Automation Test
  Scenario: Open browser and verify title
    Given I launch the Chrome browser
    When I open the Google homepage
    Then I verify the page title contains Google