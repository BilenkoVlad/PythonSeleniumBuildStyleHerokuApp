import pytest

from main.pages.dynamic_loading_page.dynamic_loading_page import DynamicLoadingPage
from main.pages.dynamic_loading_page.example1_hidden_elements_page.example1_hidden_elements_page import \
    Example1HiddenElementsPage
from main.pages.dynamic_loading_page.example2_element_rendered.example2_element_rendered import Example2ElementRendered
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0010VerifyThatElementsDynamicallyLoadedTest(BaseTest):
    dynamic_loading_page = DynamicLoadingPage()
    example1_hidden_elements_page = Example1HiddenElementsPage()
    example2_element_rendered = Example2ElementRendered()

    def test_verify_that_elements_dynamically_loaded(self):
        _BODY_TEXT = [
            "It's common to see an action get triggered that returns a result dynamically. It does not rely on the page"
            " to reload or finish loading. The page automatically gets updated (e.g. hiding elements, showing elements,"
            " updating copy, etc) through the use of JavaScript.",
            "There are two examples. One in which an element already exists on the page but it is not displayed. And "
            "anonther where the element is not on the page and gets added in."]
        _LINKS_TEXT = ["Example 1: Element on page that is hidden", "Example 2: Element rendered after the fact"]

        self.site \
            .click_on_link("Dynamic Loading")

        self.dynamic_loading_page \
            .the_page_url_contains("dynamic_loading") \
            .the_element_text_equals(self.dynamic_loading_page.HEADERS_PAGE_ELEMENT(),
                                     "Dynamically Loaded Page Elements") \
            .the_elements_in_list_equal(self.dynamic_loading_page.BODY_TEXT_ELEMENTS(), _BODY_TEXT) \
            .the_elements_in_list_equal(self.dynamic_loading_page.BODY_LINKS_ELEMENTS(), _LINKS_TEXT) \
            .click_on_first_link()

        self.example1_hidden_elements_page \
            .the_page_url_contains("dynamic_loading/1") \
            .the_element_text_equals(self.example1_hidden_elements_page.HEADERS_PAGE_ELEMENT(),
                                     "Dynamically Loaded Page Elements") \
            .the_element_text_equals(self.example1_hidden_elements_page.BODY_TEXT_ELEMENT(),
                                     "Example 1: Element on page that is hidden") \
            .the_element_is_displayed(self.example1_hidden_elements_page.START_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.example1_hidden_elements_page.START_BUTTON_ELEMENT()) \
            .click_on_start_button() \
            .the_element_text_equals(self.example1_hidden_elements_page.LOADER_ELEMENT(), "Loading...") \
            .the_element_is_displayed(self.example1_hidden_elements_page.LOADER_ELEMENT()) \
            .the_element_is_displayed_with_condition(self.example1_hidden_elements_page.HIDDEN_TEXT_XPATH()) \
            .the_element_is_displayed(self.example1_hidden_elements_page.HIDDEN_TEXT_ELEMENT()) \
            .the_element_text_equals(self.example1_hidden_elements_page.HIDDEN_TEXT_ELEMENT(), "Hello World!")

        BrowserManager().navigate_back_in_page()

        self.dynamic_loading_page \
            .click_on_second_link()

        self.example2_element_rendered \
            .the_page_url_contains("dynamic_loading/2") \
            .the_element_text_equals(self.example2_element_rendered.HEADERS_PAGE_ELEMENT(),
                                     "Dynamically Loaded Page Elements") \
            .the_element_text_equals(self.example2_element_rendered.BODY_TEXT_ELEMENT(),
                                     "Example 2: Element rendered after the fact") \
            .the_element_is_displayed(self.example2_element_rendered.START_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.example2_element_rendered.START_BUTTON_ELEMENT()) \
            .click_on_start_button() \
            .the_element_text_equals(self.example2_element_rendered.LOADER_ELEMENT(), "Loading...") \
            .the_element_is_displayed(self.example2_element_rendered.LOADER_ELEMENT()) \
            .the_element_is_displayed_with_condition(self.example2_element_rendered.HIDDEN_TEXT_XPATH()) \
            .the_element_is_displayed(self.example2_element_rendered.HIDDEN_TEXT_ELEMENT()) \
            .the_element_text_equals(self.example2_element_rendered.HIDDEN_TEXT_ELEMENT(), "Hello World!")
