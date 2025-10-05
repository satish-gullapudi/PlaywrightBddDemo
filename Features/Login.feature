Feature: Login Feature

  Scenario: Login as valid user

    Given I launch application and go to login page
    When I enter username and password
    And I submit login
    Then I should be successfully logged in