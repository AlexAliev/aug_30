from selenium.webdriver.common.by import By
class HomePage :

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://demoblaze.com/index.html')


    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
        galaxy_s6.click()


    def click_monitor(self):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()

    def check_that_product_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors) == count
