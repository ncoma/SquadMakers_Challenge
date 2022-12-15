from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By

class CartPage(PageFactory):   
    locators = {
    'btn_checkout': ('ID', "checkout"),
    'input_password': ('ID', 'password'),
    'btn_login': ('ID', 'login-button')
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def go_to_checkout(self) -> None:
        self.btn_checkout.click()

    def does_item_exist(self, item_name) -> None:
        return self.__get_item_name_element(item_name).is_enabled()

    def get_item_price(self, item_name) -> None:
        return self.__get_item_name_element(item_name).find_element(By.XPATH, f"../..//div[@class='inventory_item_price']").get_text()[1:]

    def get_items_quantity(self):
        return len(self.driver.find_elements(By.CLASS_NAME, 'cart_item'))

    def __get_item_name_element(self, item_name):
        return self.driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")



