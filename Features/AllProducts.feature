Feature: All Products Feature

  # Mention repetitive steps under 'Background'
  Background:
        Given I launch application
        When Go to all products page

  Scenario: Verify All Products and product detail page

    Then I should be navigated to ALL PRODUCTS page successfully
    And Products list is visible
#    When I click on view product of first product
#    Then I should be landed on product detail page
#    And Product detail is visible