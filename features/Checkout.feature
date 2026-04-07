Feature: Checkout Feature

  Background:
        Given I launch application
        When Go to all products page

  Scenario: Verify Register while checkout
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
    And I click Register/Login button
    And I go to signup page and fill all details
    And I submit signup
    Then New user successfully to be created
    When I get the API response
    Then New user details should be found
    When I click Continue in account creation page
    Then Verify Logged in as username at top
    When I click cart navigation link in header
    And I click proceed to checkout button
    Then Verify Address Details and Review Your Order
    When I Enter description in comment text area
    And Click Place Order CTA
    And I enter payment details like Name on Card, Card Number, CVC, Expiration date
    And I Click Pay and Confirm Order button
    Then Verify order confirmation message
    When I Click Delete Account button
    Then Verify ACCOUNT DELETED! and click Continue button
    Then I should see carousel slider in home page

