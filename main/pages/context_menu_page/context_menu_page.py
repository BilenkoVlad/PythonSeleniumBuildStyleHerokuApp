from main.pages.assertions import Assertions
from main.pages.context_menu_page.context_menu_page_functions import ContextMenuPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class ContextMenuPage(ContextMenuPageFunctions, Assertions):
    def HEADER_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADER_PAGE)

    def CONTEXT_BOX_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._CONTEXT_BOX)

    def BODY_TEXT_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._BODY_TEXT)
