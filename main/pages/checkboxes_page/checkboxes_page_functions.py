from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.logger.LoggingMixin import LoggingMixin


class CheckboxesPageFunctions(LoggingMixin):
    _HEADER_PAGE = ".//div[@class='example']/h3"
    _CHECKBOX = ".//input[@type='checkbox']"

    def select_first_checkbox(self):
        BrowserManager().find_elements_by_XPATH(self._CHECKBOX)[0].click()
        return self

    def select_second_checkbox(self):
        BrowserManager().find_elements_by_XPATH(self._CHECKBOX)[1].click()
        return self
