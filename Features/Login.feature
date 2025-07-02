Feature: Login Feature

  Scenario Outline: Validating the Login feature with valid credentials

    Given I navigate to OrangeHRM
    When I enter "<username>" and "<password>"
    And I submit login
    Then I should see dashboard
    When I click logout
    Then I should go to login page

    Examples:
      | username        | password      |
      | Admin     | admin123    |