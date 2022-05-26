import pytest
from .base_page import BasePage
from selenium.webdriver.common.by import By
from locators import MainPageLocators as MPL



class MainPage(BasePage):
    def calculate(self):
        parameter = '1*2-3+1'
        steps = {
            '1': self.browser.find_element(*MPL.ONE),
            '2': self.browser.find_element(*MPL.TWO),
            '3': self.browser.find_element(*MPL.THREE),
            '*': self.browser.find_element(*MPL.MULTIPLY),
            '-': self.browser.find_element(*MPL.MINUS),
            '+': self.browser.find_element(*MPL.PLUS),
            '=': self.browser.find_element(*MPL.EQUAL)
        }
        
        for i in range(len(parameter)):
            for step in steps:
                if parameter[i] == step:
                    steps[step].click()

        steps['='].click()

    def check_the_result(self):
        formula = self.browser.find_element(*MPL.FORMULA).text
        result = self.browser.find_element(*MPL.RESULT).text
        assert formula == '1 × 2 - 3 + 1 =', 'Incorrect formula.'
        assert result == '0', 'Incorrect answer'
