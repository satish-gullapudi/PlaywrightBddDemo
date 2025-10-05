Feature: Signup Feature

  Scenario: Signup as valid user

    Given I launch application and go to login page
    When I go to signup page and fill all details
    And I submit signup
    Then New user successfully to be created
    When I get the API response
    Then New user details should be found