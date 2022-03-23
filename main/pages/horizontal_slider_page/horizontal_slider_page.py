from main.pages.assertions import Assertions
from main.pages.horizontal_slider_page.horizontal_slider_page_functions import HorizontalSliderPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class HorizontalSliderPage(HorizontalSliderPageFunctions, Assertions):
    def HEADER_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADER_TEXT)

    def SLIDER_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._SLIDER)

    def RANGE_NUMBER_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RANGE_NUMBER)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)
