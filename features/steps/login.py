from behave import given, when, then
from hamcrest import assert_that, is_  

@given('the login page of saucedemo')
def step_impl(context): 
    context.loginPage.navigate()    

@when('I enter the the user "{user}" and its corresponding password')
def step_impl(context, user):
    context.loginPage.login_as(user)

@then('I will be redirected to the inventory page')
def step_impl(context):
    assert_that(context.inventoryPage.is_page_loaded(), is_(True))
