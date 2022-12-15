from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.your_information_page import YourInformationPage
from pages.overview_page import OverviewPage;
from pages.thank_you_page import ThankYouPage;
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_feature(context, feature):
    options = Options()
    options.add_argument("start-maximized")
    context.driver: webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.loginPage = LoginPage(context.driver)
    context.inventoryPage = InventoryPage(context.driver)
    context.cartPage = CartPage(context.driver)
    context.yourInformationPage = YourInformationPage(context.driver)
    context.overviewPage = OverviewPage(context.driver)
    context.thankYouPage = ThankYouPage(context.driver)

def after_feature(context, feature):
    context.driver.quit()
