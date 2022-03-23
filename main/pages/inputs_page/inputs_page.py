from main.pages.assertions import Assertions
from main.pages.inputs_page.inputs_page_functions import InputsPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class InputsPage(InputsPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def INPUT_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._INPUT_FIELD)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)
