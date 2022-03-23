from main.pages.assertions import Assertions
from main.pages.file_download_page.file_download_page_functions import FileDownloadPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class FileDownloadPage(FileDownloadPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def FILES_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._FILES)
