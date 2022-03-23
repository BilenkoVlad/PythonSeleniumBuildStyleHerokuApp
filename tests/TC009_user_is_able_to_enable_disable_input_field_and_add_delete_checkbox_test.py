import pytest

from main.pages.dynamic_controls_page.dynamic_controls_page import DynamicControlsPage
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC009UserIsAbleToEnableDisableInputFieldAndAddDeleteCheckboxTest(BaseTest):
    dynamic_controls_page = DynamicControlsPage()

    def test_user_is_able_to_enable_disable_input_field_and_add_delete_checkbox(self):
        _EXPECTED_HEADERS = ["Dynamic Controls", "Remove/add", "Enable/disable"]

        self.site \
            .click_on_link("Dynamic Controls")

        self.dynamic_controls_page \
            .the_page_url_contains("dynamic_controls") \
            .the_elements_in_list_equal(self.dynamic_controls_page.HEADER_PAGE_ELEMENTS(), _EXPECTED_HEADERS) \
            .the_element_text_equals(self.dynamic_controls_page.BODY_TEXT_ELEMENT(),
                                     "This example demonstrates when elements (e.g., checkbox, input field, etc.) "
                                     "are changed asynchronously.") \
            .the_element_is_unselected(self.dynamic_controls_page.CHECKBOX_ELEMENT()) \
            .the_element_is_enabled(self.dynamic_controls_page.REMOVE_BUTTON_ELEMENT()) \
            .the_element_is_displayed(self.dynamic_controls_page.REMOVE_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.dynamic_controls_page.ENABLE_BUTTON_ELEMENT()) \
            .the_element_is_displayed(self.dynamic_controls_page.ENABLE_BUTTON_ELEMENT()) \
            .the_element_is_disabled(self.dynamic_controls_page.TEXT_FIELD_ELEMENT()) \
            .click_on_checkbox() \
            .the_element_is_selected(self.dynamic_controls_page.CHECKBOX_ELEMENT()) \
            .click_on_remove_button() \
            .the_element_is_displayed(self.dynamic_controls_page.CHECKBOX_LOADING_ELEMENTS()[0]) \
            .the_element_is_displayed_with_condition(self.dynamic_controls_page.MESSAGE_XPATH()) \
            .the_element_text_equals(self.dynamic_controls_page.MESSAGE_ELEMENT(), "It's gone!") \
            .the_element_is_not_displayed(self.dynamic_controls_page.CHECKBOX_XPATH()) \
            .the_element_is_enabled(self.dynamic_controls_page.ADD_BUTTON_ELEMENT()) \
            .the_element_is_displayed(self.dynamic_controls_page.ADD_BUTTON_ELEMENT()) \
            .click_on_add_button() \
            .the_element_is_displayed(self.dynamic_controls_page.CHECKBOX_LOADING_ELEMENTS()[0]) \
            .the_element_is_displayed_with_condition(self.dynamic_controls_page.MESSAGE_XPATH()) \
            .the_element_text_equals(self.dynamic_controls_page.MESSAGE_ELEMENT(), "It's back!") \
            .the_element_is_displayed(self.dynamic_controls_page.CHECKBOX_ELEMENT()) \
            .the_element_is_unselected(self.dynamic_controls_page.CHECKBOX_ELEMENT()) \
            .click_on_enable_button() \
            .the_element_is_displayed(self.dynamic_controls_page.INPUT_LOADING_ELEMENT()) \
            .the_element_is_displayed_with_condition(self.dynamic_controls_page.MESSAGE_XPATH()) \
            .the_element_text_equals(self.dynamic_controls_page.MESSAGE_ELEMENT(), "It's enabled!") \
            .the_element_is_enabled(self.dynamic_controls_page.TEXT_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.dynamic_controls_page.DISABLE_BUTTON_ELEMENT()) \
            .the_element_is_displayed(self.dynamic_controls_page.DISABLE_BUTTON_ELEMENT()) \
            .send_keys_to_text_field("Test text is automatically added") \
            .click_on_disable_button() \
            .the_element_is_displayed(self.dynamic_controls_page.INPUT_LOADING_ELEMENT()) \
            .the_element_is_displayed_with_condition(self.dynamic_controls_page.MESSAGE_XPATH()) \
            .the_element_text_equals(self.dynamic_controls_page.MESSAGE_ELEMENT(), "It's disabled!") \
            .the_element_is_disabled(self.dynamic_controls_page.TEXT_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.dynamic_controls_page.ENABLE_BUTTON_ELEMENT()) \
            .the_element_is_displayed(self.dynamic_controls_page.ENABLE_BUTTON_ELEMENT()) \
            .the_text_equals(self.dynamic_controls_page.TEXT_FIELD_ELEMENT().get_attribute("value"),
                             "Test text is automatically added")
