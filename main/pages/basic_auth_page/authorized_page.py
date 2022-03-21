from main.pages.assertions import Assertions
from main.pages.basic_auth_page.authorized_page_functions import AuthorizedPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class AuthorizedPage(AuthorizedPageFunctions, Assertions):
    def PAGE_NAME_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._PAGE_NAME_TEXT)

    def PAGE_BODY_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._PAGE_BODY_TEXT)
