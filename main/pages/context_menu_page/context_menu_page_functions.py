from main.utils.action_manager.actions_manager import ActionsManager
from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.logger.LoggingMixin import LoggingMixin


class ContextMenuPageFunctions(LoggingMixin):
    _HEADER_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _CONTEXT_BOX = ".//div[@id='hot-spot']"

    def left_click_on_context_box(self):
        BrowserManager().find_element_by_XPATH(self._CONTEXT_BOX).click()
        return self

    def right_click_on_context_box(self):
        ActionsManager().get_actions().context_click(
            BrowserManager().find_element_by_XPATH(self._CONTEXT_BOX)).perform()
        return self

    def click_on_header(self):
        BrowserManager().find_element_by_XPATH(self._HEADER_PAGE).click()
        return self
