from seleniumpagefactory import PageFactory

class YourInformationPage(PageFactory):   
    locators = {
    'input_first_name': ('ID', "first-name"),
    'input_last_name': ('ID', 'last-name'),
    'input_zip': ('ID', 'postal-code'),
    'btn_continue': ('ID', 'continue')
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def fill_information_and_continue(self, first_name, last_name, zip) -> None:
        self.input_first_name.set_text(first_name)
        self.input_last_name.set_text(last_name)
        self.input_zip.set_text(zip)
        self.btn_continue.click()


