import pytest
from pages.main_page import MainPage


def test_simbir_soft(browser):
    url = 'https://www.google.com/'
    page = MainPage(browser, url)
    page.open()
    page.open_the_calculator()
    page.calculate()
    page.check_the_result()
