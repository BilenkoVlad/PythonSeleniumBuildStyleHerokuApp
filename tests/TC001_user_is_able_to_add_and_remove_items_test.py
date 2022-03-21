import pytest

from main.pages.add_remove_elements_page.add_remove_elements_page import AddRemoveElementsPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC001UserIsAbleToAddAndRemoveItemsTest(BaseTest):
    add_remove_elements_page = AddRemoveElementsPage()

    def test_TC001_user_is_able_to_add_and_remove_items(self):
        self.site \
            .click_on_link("Add/Remove Elements")

        self.add_remove_elements_page \
            .the_page_url_contains("add_remove_elements") \
            .click_add_button() \
            .the_element_is_displayed(web_element=self.add_remove_elements_page.ADD_BUTTON_ELEMENT()) \
            .click_delete_button() \
            .the_element_is_not_displayed(xpath=self.add_remove_elements_page.DELETE_BUTTON_XPATH()) \
            .click_add_button_10_times() \
            .the_elements_are_displayed(web_elements=self.add_remove_elements_page.DELETE_BUTTON_ELEMENTS()) \
            .the_list_size_equals(web_elements=self.add_remove_elements_page.DELETE_BUTTON_ELEMENTS(), size=10) \
            .click_delete_button_10_times() \
            .the_list_size_equals(web_elements=self.add_remove_elements_page.DELETE_BUTTON_ELEMENTS(), size=0)
