from main.pages.assertions import Assertions
from main.pages.key_presses_page.key_presses_page_functions import KeyPressesPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class KeyPressesPage(KeyPressesPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)

    def INPUT_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._INPUT_FIELD)

    def RESULT_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RESULT_TEXT)
