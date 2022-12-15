Feature: Authentication

  Background: User is authenticated
    Given the login page of saucedemo
    When I enter the the user "standard_user" and its corresponding password
    Then I will be redirected to the inventory page

  Scenario: Logout
    Given the inventory page
    When I open the burger menu and click Logout
    Then I will be sucessfully logged out and redirected to the login page
