from main.pages.assertions import Assertions
from main.pages.dynamic_controls_page.dynamic_controls_page_functions import DynamicControlsPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class DynamicControlsPage(DynamicControlsPageFunctions, Assertions):
    def HEADER_PAGE_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._HEADER_PAGE)

    def REMOVE_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._REMOVE_BUTTON)

    def ADD_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._ADD_BUTTON)

    def MESSAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MESSAGE)

    def MESSAGE_XPATH(self) -> str:
        return self._MESSAGE

    def INPUT_LOADING_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._INPUT_LOADING)

    def CHECKBOX_LOADING_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._CHECKBOX_LOADING)

    def ENABLE_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._ENABLE_BUTTON)

    def DISABLE_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._DISABLE_BUTTON)

    def CHECKBOX_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._CHECKBOX)

    def CHECKBOX_XPATH(self):
        return self._CHECKBOX

    def TEXT_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._TEXT_FIELD)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)
