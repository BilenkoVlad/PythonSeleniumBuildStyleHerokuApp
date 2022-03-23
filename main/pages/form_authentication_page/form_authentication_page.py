from main.pages.assertions import Assertions
from main.pages.form_authentication_page.form_authentication_page_functions import FormAuthenticationPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class FormAuthenticationPage(FormAuthenticationPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def CREDENTIALS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._CREDENTIALS)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)

    def USERNAME_LABEL_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._USERNAME_LABEL)

    def USERNAME_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._USERNAME_FIELD)

    def PASSWORD_LABEL_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._PASSWORD_LABEL)

    def PASSWORD_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._PASSWORD_FIELD)

    def LOGIN_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LOGIN_BUTTON)

    def LOGIN_BUTTON_LABEL_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LOGIN_BUTTON_LABEL)

    def ALERT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._ALERT)

    def MESSAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._MESSAGE)
