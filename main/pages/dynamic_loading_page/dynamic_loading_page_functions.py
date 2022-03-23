from main.utils.browser_manager.browser_manager import BrowserManager


class DynamicLoadingPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _BODY_LINKS = ".//div[@class='example']/a"

    def click_on_first_link(self):
        BrowserManager().find_elements_by_XPATH(self._BODY_LINKS)[0].click()
        return self

    def click_on_second_link(self):
        BrowserManager().find_elements_by_XPATH(self._BODY_LINKS)[1].click()
        return self
