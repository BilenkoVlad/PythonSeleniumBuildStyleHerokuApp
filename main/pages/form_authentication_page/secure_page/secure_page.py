from main.pages.assertions import Assertions
from main.pages.form_authentication_page.secure_page.secure_page_functions import SecurePageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class SecurePage(SecurePageFunctions, Assertions):

    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def LOGOUT_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LOGOUT_BUTTON)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)

    def LOGOUT_BUTTON_LABEL_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._LOGOUT_BUTTON_LABEL)

    def ALERT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._ALERT)
