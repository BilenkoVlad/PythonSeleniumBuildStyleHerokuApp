from main.utils.browser_manager.browser_manager import BrowserManager


class Example2ElementRenderedFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/h4"
    _START_BUTTON = ".//div[@id='start']/button"
    _LOADER = ".//div[@id='loading']"
    _HIDDEN_TEXT = ".//div[@id='finish']/h4"

    def click_on_start_button(self):
        BrowserManager().find_element_by_XPATH(self._START_BUTTON).click()
        return self
