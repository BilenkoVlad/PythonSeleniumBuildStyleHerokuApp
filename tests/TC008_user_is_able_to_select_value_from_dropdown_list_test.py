import pytest

from main.pages.dropdown_page.dropdown_page import DropdownPage
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC008UserIsAbleToSelectValueFromDropdownListTest(BaseTest):
    dropdown_page = DropdownPage()

    def test_user_is_able_to_select_value_from_dropdown_list(self):
        _EXPECTED_OPTIONS = ["Please select an option", "Option 1", "Option 2"]

        self.site \
            .click_on_link("Dropdown")

        self.dropdown_page \
            .the_page_url_contains("dropdown") \
            .the_element_text_equals(self.dropdown_page.HEADER_PAGE_ELEMENT(), "Dropdown List") \
            .the_element_is_displayed(self.dropdown_page.DROPDOWN_ELEMENT()) \
            .the_elements_in_list_equal(self.dropdown_page.DROPDOWN_SELECT().options, _EXPECTED_OPTIONS) \
            .select_by_visible_text(self.dropdown_page.DROPDOWN_ELEMENT(), "Option 1") \
            .the_element_text_equals(self.dropdown_page.DROPDOWN_SELECT().first_selected_option, "Option 1") \
            .select_by_visible_text(self.dropdown_page.DROPDOWN_ELEMENT(), "Option 2") \
            .the_element_text_equals(self.dropdown_page.DROPDOWN_SELECT().first_selected_option, "Option 2")

        BrowserManager().refresh_page()

        self.dropdown_page \
            .the_page_url_contains("dropdown") \
            .the_element_text_equals(self.dropdown_page.HEADER_PAGE_ELEMENT(), "Dropdown List") \
            .the_element_is_displayed(self.dropdown_page.DROPDOWN_ELEMENT()) \
            .the_elements_in_list_equal(self.dropdown_page.DROPDOWN_SELECT().options, _EXPECTED_OPTIONS)
