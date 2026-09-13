from pages.homepage import HomePage
from pages.product import ProductPage
import time

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    time.sleep(10)
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
def test_twp_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_that_product_count(2)