Feature: Cart Feature

  Background:
    Given I launch application
    When Go to all products page
    Then I should be navigated to ALL PRODUCTS page successfully

  Scenario Outline: Add multiple random products in Cart
    When I hover over and add products "<product1>" and "<product2>" to cart
    And I click on View Cart button
    Then "<product1>" and "<product2>" are added to Cart
    And Their prices, quantity and total price are correct

    Examples:
      | product1                       |  | product2             |
      | Blue Cotton Indie Mickey Dress |  | Madame Top For Women |

  Scenario: Verify Product quantity in Cart
    And Products list is visible
    When I click on view product of random product
    Then I should be landed on product detail page
    When I increase product quantity to 4
    And I click Add to Cart button
    And I click on View Cart button
    Then I should see the product that I added to the cart
    And Product price, quantity, and total quantity should be correct