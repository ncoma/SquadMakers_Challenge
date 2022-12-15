from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By

class OverviewPage(PageFactory):   
    locators = {
    'btn_finish': ('ID', 'finish'),
    'txt_subtotal':('CLASS_NAME', 'summary_subtotal_label')
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def does_item_exist(self, item_name):
        return self.__get_item_name_element(item_name).is_enabled()

    def get_item_price(self, item_name):
        return self.__get_item_name_element(item_name).find_element(By.XPATH, f"../..//div[@class='inventory_item_price']").get_text()[1:]

    def get_items_quantity(self):
        return len(self.driver.find_elements(By.CLASS_NAME, 'cart_item'))

    def get_subtotal_text(self):
        return self.txt_subtotal.get_text()

    def complete_checkout(self):
        return self.btn_finish.click()

    def __get_item_name_element(self, item_name):
        return self.driver.find_element(By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")

        

