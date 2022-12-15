from behave import given, when, then
from hamcrest import assert_that, is_, equal_to

@given('the following items added to the cart')
def step_impl(context):
    context.inventoryPage.add_items_to_cart(context.table)
    context.testTable = context.table

@when('I continue to the cart page')
def step_impl(context):
    context.inventoryPage.go_to_cart()

@when('I continue to the checkout page')
def step_impl(context):
    context.inventoryPage.go_to_cart()
    context.cartPage.go_to_checkout()

@when('I fill the information required with "{first_name}", "{last_name}", "{zip}"')
def step_impl(context, first_name, last_name, zip):
    context.yourInformationPage.fill_information_and_continue(first_name, last_name, zip)

@then('the added items will be shown with their respective prices')
def step_impl(context):
    cartTotalItems = 0
    for row in context.testTable:
        itemExist = context.cartPage.does_item_exist(row['item_name'])
        itemPrice = context.cartPage.get_item_price(row['item_name'])
        cartTotalItems += 1

        assert_that(itemExist, is_(True))
        assert_that(itemPrice, equal_to(row['price']))
    context.cartTotalItems = cartTotalItems

@then('the numbers of items displayed in the cart will match the number of items added')
def step_impl(context):
    assert_that(context.cartPage.get_items_quantity(), equal_to(context.cartTotalItems))

@then('I will see the items added with their respective prices')
def step_impl(context):
    expectedTotal = 0
    totalItems = 0
    for row in context.testTable:
        itemExist = context.overviewPage.does_item_exist(row['item_name'])
        itemPrice = context.overviewPage.get_item_price(row['item_name'])
        expectedTotal += float(itemPrice)
        totalItems += 1

        assert_that(itemExist, is_(True))
        assert_that(itemPrice, equal_to(row['price']))
    context.totalItems = totalItems
    context.expectedTotal = expectedTotal

@then('the numbers of items displayed will match the number of items added')
def step_impl(context):
    assert_that(context.overviewPage.get_items_quantity(), equal_to(context.totalItems))

@then('the subtotal will match the sum of the items prices')
def step_impl(context):
    assert_that(context.overviewPage.get_subtotal_text(), equal_to(f"Item total: ${context.expectedTotal}"))
    context.overviewPage.complete_checkout()

    
@then('I will be able to finish and see the Thank You page')
def step_impl(context):
    return context.thankYouPage.is_page_loaded()