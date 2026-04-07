Feature: Contact Us Feature

  Scenario: Contact Us Form

    Given I launch application
    When I go to contact us page
    Then Get in touch text is visible
    When I fill contact us form
    And I upload file
    When I submit contact us form
    Then I should see success message
    When I click home button
    Then I should land on home page