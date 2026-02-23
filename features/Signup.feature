Feature: Signup Feature

  # Mention repetitive steps under 'Background'
  Background:
        Given I launch application
        When Go to login/signup page

  Scenario: Signup as valid user

#    Given I launch application
#    When Go to login/signup page
    When I go to signup page and fill all details
    And I submit signup
    Then New user successfully to be created
    When I get the API response
    Then New user details should be found

  Scenario: Signup as existing user

#    Given I launch application
#    When Go to login/signup page
    When I signup with existing user details
    Then I should see error message