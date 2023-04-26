from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage():


    URL = 'https://www.saucedemo.com/'
    SEARCH_FIELD = (By.XPATH, '//input[@name="user-name"]')
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(url=self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        search_input.send_keys(phrase + Keys.RETURN)