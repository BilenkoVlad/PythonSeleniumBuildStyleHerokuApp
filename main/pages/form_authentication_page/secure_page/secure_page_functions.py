from main.utils.browser_manager.browser_manager import BrowserManager


class SecurePageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h2"
    _BODY_TEXT = ".//div[@class='example']/h4"
    _ALERT = ".//div[@id='flash-messages']"
    _LOGOUT_BUTTON = ".//a[@class='button secondary radius']"
    _LOGOUT_BUTTON_LABEL = ".//a[@class='button secondary radius']/i"

    def click_logout_button(self):
        BrowserManager().find_element_by_XPATH(self._LOGOUT_BUTTON).click()
        return self
