from main.utils.browser_manager.browser_manager import BrowserManager


class FormAuthenticationPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h2"
    _BODY_TEXT = ".//div[@class='example']/h4"
    _CREDENTIALS = ".//div[@class='example']/h4/em"
    _USERNAME_LABEL = ".//label[@for='username']"
    _USERNAME_FIELD = ".//input[@name='username']"
    _PASSWORD_LABEL = ".//label[@for='password']"
    _PASSWORD_FIELD = ".//input[@name='password']"
    _LOGIN_BUTTON = ".//button"
    _LOGIN_BUTTON_LABEL = ".//button/i"
    _ALERT = "//div[@id='flash-messages']"
    _MESSAGE = ".//div[@id='flash']"

    def send_keys_to_field(self, web_element, value):
        web_element.send_keys(value)
        return self

    def click_login_button(self):
        BrowserManager().find_element_by_XPATH(self._LOGIN_BUTTON).click()
        return self
