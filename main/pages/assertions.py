from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.browser_manager.driver import get_driver
from main.utils.logger.LoggingMixin import LoggingMixin


class Assertions(LoggingMixin):

    def the_element_is_displayed(self, web_element):
        assert web_element.is_displayed(), "Web element is not displayed"
        return self

    def the_element_is_enabled(self, web_element):
        assert web_element.is_enabled(), "Web element is not enabled"
        return self

    def the_element_is_disabled(self, web_element):
        assert not web_element.is_enabled(), "Web element is not disabled"
        return self

    def the_polling_condition(self, condition):
        try:
            while not condition():
                BrowserManager().refresh_page()
            return self
        except:
            return self

    def the_element_is_not_displayed(self, xpath):
        try:
            assert not BrowserManager().find_element_by_XPATH(xpath).is_displayed(), "element is displayed"
        except:
            assert True
        return self

    def the_elements_are_displayed(self, web_elements):
        for web_element in web_elements:
            assert web_element.is_displayed()
        return self

    def the_list_size_equals(self, web_elements, size=None, expected_list=None):
        if size is None:
            assert len(web_elements) == len(expected_list)
        else:
            assert len(web_elements) == size
        return self

    def the_element_text_equals(self, web_element, expected_text):
        self.logger.debug(f"Text from web element is {web_element.text}. Expected text is {expected_text}")
        assert web_element.text.strip(), expected_text
        return self

    def the_alert_text_equals(self, expected_text):
        self.logger.debug(f"{get_driver().switch_to.alert.text} text is displayed")
        assert get_driver().switch_to.alert.text, expected_text
        return self

    def the_page_url_contains(self, url):
        assert url in BrowserManager().get_current_url()
        return self

    def the_element_is_selected(self, web_element):
        assert web_element.is_selected()
        return self

    def the_element_is_unselected(self, web_element):
        assert not web_element.is_selected()
        return self

    def the_elements_in_list_equal(self, web_elements, expected_list):
        for i in range(len(web_elements)):
            assert web_elements[i].text == expected_list[i]
        return self

    def the_text_equals(self, text1, text2):
        assert text1 == text2
        return self

    def the_element_is_displayed_with_condition(self, xpath):
        WebDriverWait(get_driver(), 10).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        return self

    def the_alert_is_presented(self):
        try:
            WebDriverWait(get_driver(), 10).until(expected_conditions.alert_is_present())
            assert True
        except:
            assert False
        return self

    def the_alert_is_not_presented(self):
        try:
            BrowserManager().switch_to_alert()
            assert False
        except:
            assert True
        return self
