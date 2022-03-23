from main.pages.assertions import Assertions
from main.pages.forgot_password_page.forgot_password_page_functions import ForgotPasswordPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class ForgotPasswordPage(ForgotPasswordPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def FIELD_LABEL_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._FIELD_LABEL)

    def EMAIL_FIELD_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._EMAIL_FIELD)

    def RETRIEVE_PASSWORD_BUTTON_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RETRIEVE_PASSWORD_BUTTON)

    def BUTTON_NAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BUTTON_NAME)
