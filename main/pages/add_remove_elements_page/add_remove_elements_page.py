from main.pages.add_remove_elements_page.add_remove_elements_page_functions import AddRemoveElementsPageFunctions
from main.pages.assertions import Assertions
from main.utils.browser_manager.browser_manager import BrowserManager


class AddRemoveElementsPage(AddRemoveElementsPageFunctions, Assertions):
    def ADD_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._ADD_BUTTON)

    def DELETE_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._DELETE_BUTTON)

    def DELETE_BUTTON_XPATH(self):
        return self._DELETE_BUTTON

    def DELETE_BUTTON_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._DELETE_BUTTON)
