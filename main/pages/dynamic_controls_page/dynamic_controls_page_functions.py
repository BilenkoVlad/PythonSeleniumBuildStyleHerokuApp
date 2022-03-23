from main.utils.browser_manager.browser_manager import BrowserManager


class DynamicControlsPageFunctions:
    _HEADER_PAGE = ".//div[@class='example']/h4"
    _BODY_TEXT = ".//div[@class='example']/p"
    _REMOVE_BUTTON = ".//button[text()='Remove']"
    _ADD_BUTTON = ".//button[text()='Add']"
    _MESSAGE = ".//p[@id='message']"
    _INPUT_LOADING = ".//form[@id='input-example']//div[@id='loading']"
    _CHECKBOX_LOADING = ".//form[@id='checkbox-example']//div[@id='loading']"
    _ENABLE_BUTTON = ".//button[text()='Enable']"
    _DISABLE_BUTTON = ".//button[text()='Disable']"
    _CHECKBOX = ".//input[@type='checkbox']"
    _TEXT_FIELD = ".//input[@type='text']"

    def click_on_checkbox(self):
        BrowserManager().find_element_by_XPATH(self._CHECKBOX).click()
        return self

    def click_on_remove_button(self):
        BrowserManager().find_element_by_XPATH(self._REMOVE_BUTTON).click()
        return self

    def click_on_add_button(self):
        BrowserManager().find_element_by_XPATH(self._ADD_BUTTON).click()
        return self

    def click_on_enable_button(self):
        BrowserManager().find_element_by_XPATH(self._ENABLE_BUTTON).click()
        return self

    def click_on_disable_button(self):
        BrowserManager().find_element_by_XPATH(self._DISABLE_BUTTON).click()
        return self

    def send_keys_to_text_field(self, value):
        BrowserManager().find_element_by_XPATH(self._TEXT_FIELD).send_keys(value)
        return self
