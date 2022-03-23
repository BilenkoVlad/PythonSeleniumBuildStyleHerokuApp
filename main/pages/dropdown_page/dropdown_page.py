from selenium.webdriver.support.select import Select

from main.pages.assertions import Assertions
from main.pages.dropdown_page.dropdown_page_functions import DropdownPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class DropdownPage(DropdownPageFunctions, Assertions):
    def HEADER_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADER_PAGE)

    def DROPDOWN_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._DROPDOWN)

    def DROPDOWN_SELECT(self):
        return Select(self.DROPDOWN_ELEMENT())
