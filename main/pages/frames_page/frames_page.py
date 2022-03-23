from main.pages.assertions import Assertions
from main.pages.frames_page.frames_page_functions import FramesPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class FramesPage(FramesPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENTS(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def LINKS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._LINKS)
