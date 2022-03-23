from main.utils.browser_manager.browser_manager import BrowserManager


class FileDownloadPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _FILES = ".//div[@class='example']/a"

    def click_on_files_links(self):
        for web_element in BrowserManager().find_elements_by_XPATH(self._FILES):
            web_element.click()
        return self
