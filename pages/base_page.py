from locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    def open_the_calculator(self):
        input = self.browser.find_element(*BasePageLocators.INPUT)
        input.send_keys('Калькулятор')
        btn = self.browser.find_element(*BasePageLocators.SEARCH_BTN)
        btn.click()
