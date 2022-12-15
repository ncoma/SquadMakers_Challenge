from seleniumpagefactory import PageFactory

class LoginPage(PageFactory):
    URL = "https://www.saucedemo.com/"
    
    locators = {
    'input_user_name': ('ID', "user-name"),
    'input_password': ('ID', 'password'),
    'btn_login': ('ID', 'login-button')
    }

    def __init__(self, driver) -> None:
        self.driver = driver

    def navigate(self) -> None:
        self.driver.get(self.URL)

    def login_as(self, user) -> None:
        self.driver.get(self.URL)
        self.input_user_name.set_text(user)
        self.input_password.set_text("secret_sauce")
        self.btn_login.click()
    
    def is_page_loaded(self):
        return self.input_user_name.is_enabled()
