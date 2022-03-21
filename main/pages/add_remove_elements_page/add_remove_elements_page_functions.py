from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.logger.LoggingMixin import LoggingMixin


class AddRemoveElementsPageFunctions(LoggingMixin):
    _ADD_BUTTON = "//button[@onclick='addElement()']"
    _DELETE_BUTTON = "//button[@onclick='deleteElement()']"

    def click_add_button(self):
        BrowserManager().find_element_by_XPATH(self._ADD_BUTTON).click()
        self.logger.debug(f"Click on element with XPATH {self._ADD_BUTTON}")
        return self

    def click_delete_button(self):
        BrowserManager().find_element_by_XPATH(self._DELETE_BUTTON).click()
        self.logger.debug(f"Click on element with XPATH {self._DELETE_BUTTON}")
        return self

    def click_add_button_10_times(self):
        for i in range(10):
            BrowserManager().find_element_by_XPATH(self._ADD_BUTTON).click()
            self.logger.debug(f"Click on element with XPATH {self._ADD_BUTTON}")
        return self

    def click_delete_button_10_times(self):
        items = len(BrowserManager().find_elements_by_XPATH(self._DELETE_BUTTON)) - 1
        while items >= 0:
            BrowserManager().find_elements_by_XPATH(self._DELETE_BUTTON)[items].click()
            self.logger.debug(f"Click on element with XPATH {self._DELETE_BUTTON}")
            items -= 1
        return self
