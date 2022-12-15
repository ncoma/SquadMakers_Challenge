from behave import given, when, then
from hamcrest import assert_that, is_

@given('the inventory page')
def step_impl(context):
    pass

@when('I open the burger menu and click Logout')
def step_impl(context):
    context.inventoryPage.logout()

@then('I will be sucessfully logged out and redirected to the login page')
def step_impl(context):
    assert_that(context.loginPage.is_page_loaded(), is_(True))
