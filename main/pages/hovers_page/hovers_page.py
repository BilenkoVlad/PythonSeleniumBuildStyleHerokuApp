from main.pages.assertions import Assertions
from main.pages.hovers_page.hovers_page_functions import HoversPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class HoversPage(HoversPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def AVATARS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._AVATARS)

    def AVATARS_NAMES_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._AVATARS_NAMES)

    def AVATARS_LINKS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._AVATARS_LINKS)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)
