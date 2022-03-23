from main.utils.browser_manager.browser_manager import BrowserManager


class FramesPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _LINKS = ".//div[@class='example']/ul/li/a"

    def click_on_nested_frames_link(self):
        BrowserManager().find_elements_by_XPATH(self._LINKS)[0].click()
        return self

    def click_on_iFrame_link(self):
        BrowserManager().find_elements_by_XPATH(self._LINKS)[1].click()
        return self
