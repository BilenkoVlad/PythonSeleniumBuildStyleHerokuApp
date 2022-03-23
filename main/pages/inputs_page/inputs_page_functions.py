from main.utils.browser_manager.browser_manager import BrowserManager


class InputsPageFunctions:
    _HEADERS_PAGE = ".//div[@class='large-6 small-12 columns large-centered']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _INPUT_FIELD = ".//input"

    def click_on_input_field(self):
        BrowserManager().find_element_by_XPATH(self._INPUT_FIELD).click()
        return self

    def send_keys_to_input_field(self, value):
        BrowserManager().find_element_by_XPATH(self._INPUT_FIELD).send_keys(value)
        return self

    def clear_input_field(self):
        BrowserManager().find_element_by_XPATH(self._INPUT_FIELD).clear()
        return self
