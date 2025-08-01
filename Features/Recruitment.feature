Feature: Recruitment Feature

  Scenario Outline: Creating new candidate

    Given I navigate to OrangeHRM
    When I enter "<username>" and "<password>"
    And I submit login
    When I go to Recruitment module
    And I create new candidate
    Then Candidate should be displayed in recruitment dashboard

    Examples:
      | username        | password      |
      | Admin     | admin123    |