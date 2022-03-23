from main.pages.assertions import Assertions
from main.pages.java_script_alerts_page.java_script_alerts_page_functions import JavaScriptAlertsPageFunctions
from main.utils.browser_manager.browser_manager import BrowserManager


class JavaScriptAlertsPage(JavaScriptAlertsPageFunctions, Assertions):
    def HEADERS_PAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._HEADERS_PAGE)

    def RESULT_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RESULT_TEXT)

    def BODY_TEXT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._BODY_TEXT)

    def RESULT_MESSAGE_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._RESULT_MESSAGE)

    def JS_BUTTONS_ELEMENTS(self):
        return BrowserManager().find_elements_by_XPATH(self._JS_BUTTONS)

    def JS_ALERT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._JS_ALERT)

    def JS_CONFIRM_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._JS_CONFIRM)

    def JS_PROMPT_ELEMENT(self):
        return BrowserManager().find_element_by_XPATH(self._JS_PROMPT)
