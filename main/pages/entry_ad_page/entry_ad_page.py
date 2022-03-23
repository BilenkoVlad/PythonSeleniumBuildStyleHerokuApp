from main.pages.assertions import Assertions
from main.pages.entry_ad_page.entry_ad_page_functions import EntryAdPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class EntryAdPage(EntryAdPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def MODAL_WINDOW_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MODAL_WINDOW)

    def MODAL_WINDOW_XPATH(self):
        return self._MODAL_WINDOW

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_elements_by_XPATH(self._BODY_TEXT)

    def CLICK_HERE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._CLICK_HERE)

    def TITLE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._TITLE)

    def TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._TEXT)

    def CLOSE_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._CLOSE_BUTTON)
