Feature: Search Product Feature

  # Mention repetitive steps under 'Background'
  Background:
    Given I launch application
    When Go to all products page

  Scenario: Search product and add to cart page
    Then I should be navigated to ALL PRODUCTS page successfully
    And Products list is visible
    When I click on view product of random product
    Then I should be landed on product detail page
    When I click Add to Cart button
    Then I should see product has been added confirmation popup
    When I click on View Cart button
    Then I should navigate to view cart page
    And I should see the product that I added to the cart
    When I click proceed to checkout button
    Then I should see checkout popup asking register or login to checkout
    When I click Register/Login button
    Then I should navigate to login page
    When I enter username and password
    And I submit login
    Then I should be successfully logged in
    When I click cart navigation link in header
    Then I should see the product that I added to the cart