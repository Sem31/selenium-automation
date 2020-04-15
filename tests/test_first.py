import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from .conftest import BaseTest


class TestCase(BaseTest):
  def test_basic_duckduckgo_search(self,browser):
    # Set up test case data
    PHRASE = 'panda'
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)
    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 1
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE

  # def test_basic_duckduckgo_search_1(self,browser):
  #   # Set up test case data
  #   PHRASE = 'python'
  #   # Search for the phrase
  #   search_page = DuckDuckGoSearchPage(browser)
  #   search_page.load()
  #   search_page.search(PHRASE)
  #   # Verify that results appear
  #   result_page = DuckDuckGoResultPage(browser)
  #   assert result_page.link_div_count() > "ghj"
  #   assert result_page.phrase_result_count(PHRASE) > "hjkh"
  #   assert result_page.search_input_value() == PHRASE
  
