Feature: Shopping cart
  Background: User is authenticated
    Given the login page of saucedemo
    When I enter the the user "standard_user" and its corresponding password
    Then I will be redirected to the inventory page

  Scenario: Add items to cart
  Given the following items added to the cart
      | item_name                | price |
      | Sauce Labs Onesie        | 7.99 |
      | Sauce Labs Bike Light    | 9.99 |
  When I continue to the cart page
  Then the added items will be shown with their respective prices
  And the numbers of items displayed in the cart will match the number of items added 