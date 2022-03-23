from selenium.webdriver.common.keys import Keys

from main.pages.assertions import Assertions
from main.utils.action_manager.actions_manager import ActionsManager
from main.utils.browser_manager.browser_manager import BrowserManager


class HorizontalSliderPageFunctions:
    _HEADER_TEXT = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/h4"
    _SLIDER = ".//input"
    _RANGE_NUMBER = ".//span[@id='range']"
    _range_values_keyboard = ["0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "5"]
    _range_values_up_mouse = ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "3.5", "4", "4.5", "5"]
    _rangeValuesDown = ["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4", "4.5"]
    _assertions = Assertions()

    def move_slider_up_by_mouse_with_assertion(self):
        j = 0
        for i in range(-25, 30, 5):
            ActionsManager().get_actions().move_to_element(BrowserManager().find_element_by_XPATH(self._SLIDER))
            ActionsManager().get_actions().move_by_offset(i, 0).click().perform()
            self._assertions.the_element_text_equals(BrowserManager().find_element_by_XPATH(self._RANGE_NUMBER),
                                                     self._rangeValuesDown[j])
            j += 1
        return self

    def move_slider_down_by_mouse_with_assertion(self):
        j = len(self._rangeValuesDown) - 1
        for i in range(25, -30, 5):
            ActionsManager().get_actions().move_to_element_with_offset(BrowserManager().find_element_by_XPATH(self._SLIDER))
            ActionsManager().get_actions().move_by_offset(i, 0).click().perform()
            self._assertions.the_element_text_equals(BrowserManager().find_element_by_XPATH(self._RANGE_NUMBER),
                                                     self._rangeValuesDown[j])
            j -= 1
        return self

    def move_slider_up_by_keyboard_with_assertion(self):
        for i in range(0, 50, 5):
            ActionsManager().get_actions().move_to_element_with_offset(
                BrowserManager().find_element_by_XPATH(self._SLIDER), -25, 0)
            self.send_keys_to_slider(Keys.ARROW_UP)
            self._assertions \
                .the_element_text_equals(BrowserManager().find_element_by_XPATH(self._RANGE_NUMBER),
                                         self._range_values_keyboard[int(i / 5)])
        return self

    def move_slider_down_by_keyboard_with_assertion(self):
        for i in range(45, 0, -5):
            ActionsManager().get_actions().move_to_element_with_offset(
                BrowserManager().find_element_by_XPATH(self._SLIDER), -25, 0)
            self.send_keys_to_slider(Keys.ARROW_DOWN)
            self._assertions \
                .the_element_text_equals(BrowserManager().find_element_by_XPATH(self._RANGE_NUMBER),
                                         self._range_values_keyboard[int(i / 5)])
        return self

    def send_keys_to_slider(self, value):
        BrowserManager().find_element_by_XPATH(self._SLIDER).send_keys(value)
        return self
