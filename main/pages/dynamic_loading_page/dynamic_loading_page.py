from main.pages.assertions import Assertions
from main.pages.dynamic_loading_page.dynamic_loading_page_functions import DynamicLoadingPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class DynamicLoadingPage(DynamicLoadingPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def BODY_LINKS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._BODY_LINKS)

    def BODY_TEXT_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._BODY_TEXT)