Feature: Login Feature

  Scenario: Login as valid user

    Given I launch application and go to login page
    When I enter username and password
    And I submit login
    Then I should be successfully logged in

  Scenario: Login as invalid user

    Given I launch application and go to login page
    When I enter invalid username and password
    And I submit login
    Then I should see invalid user error message

  Scenario: Logout user

    Given I launch application and go to login page
    When I enter username and password
    And I submit login
    Then I should be successfully logged in
    When I click logout button
    Then I should navigate to login page