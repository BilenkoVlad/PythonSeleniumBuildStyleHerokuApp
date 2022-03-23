from main.utils.browser_manager.browser_manager import BrowserManager


class ForgotPasswordPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h2"
    _FIELD_LABEL = ".//label[@for='email']"
    _EMAIL_FIELD = ".//input[@id='email']"
    _RETRIEVE_PASSWORD_BUTTON = ".//button[@id='form_submit']"
    _BUTTON_NAME = ".//button[@id='form_submit']/i"

    def send_keys_to_email_field(self, value):
        BrowserManager().find_element_by_XPATH(self._EMAIL_FIELD).send_keys(value)
        return self

    def click_on_retrieve_password_button(self):
        BrowserManager().find_element_by_XPATH(self._RETRIEVE_PASSWORD_BUTTON).click()
        return self
