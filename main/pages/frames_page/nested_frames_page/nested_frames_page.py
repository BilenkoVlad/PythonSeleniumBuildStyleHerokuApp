from main.pages.assertions import Assertions
from main.pages.frames_page.nested_frames_page.nested_frames_page_functions import NestedFramesPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class NestedFramesPage(NestedFramesPageFunctions, Assertions):
    def MIDDLE_FRAME_SET_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MIDDLE_FRAME_SET)

    def LEFT_FRAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LEFT_FRAME)

    def MIDDLE_FRAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MIDDLE_FRAME)

    def RIGHT_FRAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RIGHT_FRAME)

    def BOTTOM_FRAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BOTTOM_FRAME)

    def TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._TEXT)

    def MIDDLE_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MIDDLE_TEXT)
