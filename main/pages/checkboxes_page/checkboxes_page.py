from main.pages.assertions import Assertions
from main.pages.checkboxes_page.checkboxes_page_functions import CheckboxesPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class CheckboxesPage(CheckboxesPageFunctions, Assertions):
    def HEADER_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADER_PAGE)

    def CHECKBOX_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._CHECKBOX)
