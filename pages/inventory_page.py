from seleniumpagefactory import PageFactory
from re import sub

class InventoryPage(PageFactory):
    locators = {
    'app_logo': ('CLASS_NAME', "app_logo"),
    'btn_shopping_cart': ('CLASS_NAME', "shopping_cart_link"),
    'btn_burguer_menu': ('ID', 'react-burger-menu-btn'),
    'btn_logout': ('ID', 'logout_sidebar_link')
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def is_page_loaded(self) -> None:
        return self.app_logo.is_enabled()

    def add_items_to_cart(self, table) -> None:
        for row in table:
            item_locator = 'add-to-cart-' + self.__kebab(row['item_name'])
            self.driver.find_element('id', item_locator).click()

    def go_to_cart(self) -> None:
        self.btn_shopping_cart.click()

    def logout(self) -> None:
        self.btn_burguer_menu.click()
        self.btn_logout.click()

    def __kebab(self, s):
        return s.replace(' ','-', -1).lower()




    

