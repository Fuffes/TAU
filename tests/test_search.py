import pytest
import selenium
from selenium import webdriver
from pages.search import SearchPage
from pages.result import ResultPage
@pytest.mark.parametrize('login', ['panda', 'standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user'])
def test_basic_duckduckgo_search(browser, login):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)

    search_page.load()

    search_page.search(login)



