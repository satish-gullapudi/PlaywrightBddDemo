Feature: Login Feature

  # Mention repetitive steps under 'Background'
  Background:
        Given I launch application
        When Go to login/signup page

  Scenario: Login as valid user

    When I enter username and password
    And I submit login
    Then I should be successfully logged in

  Scenario: Login as invalid user

    When I enter invalid username and password
    And I submit login
    Then I should see invalid user error message

  Scenario: Logout user

    When I enter username and password
    And I submit login
    Then I should be successfully logged in
    When I click logout button
    Then I should navigate to login page