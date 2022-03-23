from main.utils.browser_manager.browser_manager import BrowserManager


class JavaScriptAlertsPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _RESULT_TEXT = ".//div[@class='example']/h4"
    _RESULT_MESSAGE = ".//p[@id='result']"
    _JS_BUTTONS = ".//button"
    _JS_ALERT = ".//button[@onclick='jsAlert()']"
    _JS_CONFIRM = ".//button[@onclick='jsConfirm()']"
    _JS_PROMPT = ".//button[@onclick='jsPrompt()']"

    def click_on_js_alert(self):
        BrowserManager().find_element_by_XPATH(self._JS_ALERT).click()
        return self

    def click_on_js_confirm(self):
        BrowserManager().find_element_by_XPATH(self._JS_CONFIRM).click()
        return self

    def click_on_js_prompt(self):
        BrowserManager().find_element_by_XPATH(self._JS_PROMPT).click()
        return self
