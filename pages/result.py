
from selenium.webdriver.common.by import By


class ResultPage():

    RESULT_LINKS = (By.CLASS_NAME, 'EKtkFWMYpwzMKOYr0GYm LQVY1Jpkk8nyJ6HBWKAk')
    SEARCH_INPUT = (By.XPATH, "//input[@id = 'search_form_input']")
    def __init__(self, browser):
        self.browser = browser

    def link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [links.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        val = search_input.get_attribute('value')
        return val

    def title(self):
        return self.browser.title



print()