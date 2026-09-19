Feature: Data-Driven Login Automation

  Scenario Outline: Verify login with multiple data sets
    Given I navigate to the login page
    When I enter "<username>" and "<password>"
    Then I validate the login result

    Examples:
      | username      | password        |
      | standard_user | secret_password |
      | locked_user   | wrong_password  |