Feature: Subscription Feature

  Background:
    Given I launch application

  Scenario Outline: Verify Subscription on <page_name>
    Given I navigate to the "<page_name>"
    When I scroll down to footer
    Then I should see subscription section
    When I enter "<email>" in subscription email input box
    And Click Subscription field arrow button
    Then I should see subscription success message

    Examples:
      | page_name |  email              |
      | Home      |  test@yopmail.com   |
      | Cart      |  test2@yopmail.com  |