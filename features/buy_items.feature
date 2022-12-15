Feature: Buy one or multiple items
  Background: User is authenticated
    Given the login page of saucedemo
    When I enter the the user "standard_user" and its corresponding password
    Then I will be redirected to the inventory page

  Scenario: Add one item and complete checkout
    Given the following items added to the cart
      | item_name                         | price |
      | Test.allTheThings() T-Shirt (Red) | 15.99 |
    When I continue to the checkout page
    And I fill the information required with "TestFN", "TestLN", "01012"
    Then I will see the items added with their respective prices
    And the numbers of items displayed will match the number of items added
    And the subtotal will match the sum of the items prices
    And I will be able to finish and see the Thank You page

  Scenario: Add multiple items and complete checkout
    Given the following items added to the cart
      | item_name                | price |
      | Sauce Labs Backpack      | 29.99 |
      | Sauce Labs Fleece Jacket | 49.99 |
      | Sauce Labs Bolt T-Shirt  | 15.99 |
    When I continue to the checkout page
    And I fill the information required with "TestFN", "TestLN", "01012"
    Then I will see the items added with their respective prices
    And the numbers of items displayed will match the number of items added
    And the subtotal will match the sum of the items prices
    And I will be able to finish and see the Thank You page
