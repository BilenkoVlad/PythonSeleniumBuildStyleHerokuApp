from main.pages.assertions import Assertions
from main.pages.dynamic_loading_page.example1_hidden_elements_page.example1_hidden_elements_page_functions import \
    Example1HiddenElementsPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class Example1HiddenElementsPage(Example1HiddenElementsPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def START_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._START_BUTTON)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)

    def LOADER_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LOADER)

    def HIDDEN_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HIDDEN_TEXT)

    def HIDDEN_TEXT_XPATH(self):
        return self._HIDDEN_TEXT
