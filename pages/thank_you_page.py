from seleniumpagefactory import PageFactory

class ThankYouPage(PageFactory):    
    locators = {
    'container_checkout_complete': ('ID', "checkout_complete_container")
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def is_page_loaded(self):
        return self.container_checkout_complete.is_enabled()

