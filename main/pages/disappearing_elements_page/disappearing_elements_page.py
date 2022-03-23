from main.pages.assertions import Assertions
from main.pages.disappearing_elements_page.disappearing_elements_page_functions import DisappearingElementsPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class DisappearingElementsPage(DisappearingElementsPageFunctions, Assertions):
    def HEADER_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADER_PAGE)

    def BUTTON_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._BUTTON)

    def HIDDEN_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HIDDEN_BUTTON)

    def HIDDEN_BUTTON_XPATH(self):
        return self._HIDDEN_BUTTON

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)
