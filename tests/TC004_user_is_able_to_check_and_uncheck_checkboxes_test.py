import pytest

from main.pages.checkboxes_page.checkboxes_page import CheckboxesPage
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC004UserIsAbleToCheckAndUncheckCheckboxesTest(BaseTest):
    checkboxes_page = CheckboxesPage()

    def test_TC004_user_is_able_to_check_and_uncheck_checkboxes(self):
        self.site \
            .click_on_link("Checkboxes")

        self.checkboxes_page \
            .the_page_url_contains("checkboxes") \
            .the_element_text_equals(self.checkboxes_page.HEADER_PAGE_ELEMENT(), "Checkboxes") \
            .the_element_is_unselected(self.checkboxes_page.CHECKBOX_ELEMENTS()[0]) \
            .the_element_is_selected(self.checkboxes_page.CHECKBOX_ELEMENTS()[1]) \
            .select_first_checkbox() \
            .the_element_is_selected(self.checkboxes_page.CHECKBOX_ELEMENTS()[0]) \
            .select_first_checkbox() \
            .select_second_checkbox() \
            .the_element_is_unselected(self.checkboxes_page.CHECKBOX_ELEMENTS()[0]) \
            .the_element_is_unselected(self.checkboxes_page.CHECKBOX_ELEMENTS()[1]) \
            .select_first_checkbox() \
            .the_element_is_selected(self.checkboxes_page.CHECKBOX_ELEMENTS()[0])

        BrowserManager().refresh_page()

        self.checkboxes_page \
            .the_page_url_contains("checkboxes") \
            .the_element_text_equals(self.checkboxes_page.HEADER_PAGE_ELEMENT(), "Checkboxes") \
            .the_element_is_unselected(self.checkboxes_page.CHECKBOX_ELEMENTS()[0]) \
            .the_element_is_selected(self.checkboxes_page.CHECKBOX_ELEMENTS()[1])
