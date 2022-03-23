import pytest

from main.pages.entry_ad_page.entry_ad_page import EntryAdPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0011UserIsAbleToSeeModalWindowAndCanCloseItTest(BaseTest):
    entry_ad_page = EntryAdPage()

    def test_user_is_able_to_see_modal_window_and_can_close_it(self):
        _TEXT = ["Displays an ad on page load.", "If closed, it will not appear on subsequent page loads.",
                 "To re-enable it, click here."]
        self.site \
            .click_on_link("Entry Ad")

        self.entry_ad_page \
            .the_page_url_contains("entry_ad") \
            .the_element_is_displayed_with_condition(self.entry_ad_page.MODAL_WINDOW_XPATH()) \
            .the_element_text_equals(self.entry_ad_page.TITLE_ELEMENT(), "This is a modal window".upper()) \
            .the_element_text_equals(self.entry_ad_page.TEXT_ELEMENT(),
                                     "It's commonly used to encourage a user to take an action (e.g., give their "
                                     "e-mail address to sign up for something or disable their ad blocker).") \
            .the_element_text_equals(self.entry_ad_page.CLOSE_BUTTON_ELEMENT(), "Close") \
            .click_close_button() \
            .the_element_text_equals(self.entry_ad_page.HEADERS_PAGE_ELEMENT(), "Entry Ad") \
            .the_elements_in_list_equal(self.entry_ad_page.BODY_TEXT_ELEMENT(), _TEXT) \
            .the_element_is_displayed(self.entry_ad_page.CLICK_HERE_ELEMENT()) \
            .click_on_click_here() \
            .the_element_is_displayed_with_condition(self.entry_ad_page.MODAL_WINDOW_XPATH()) \
            .the_element_text_equals(self.entry_ad_page.TITLE_ELEMENT(), "This is a modal window".upper()) \
            .the_element_text_equals(self.entry_ad_page.TEXT_ELEMENT(),
                                     "It's commonly used to encourage a user to take an action (e.g., give their "
                                     "e-mail address to sign up for something or disable their ad blocker).") \
            .the_element_text_equals(self.entry_ad_page.CLOSE_BUTTON_ELEMENT(), "Close") \
            .click_close_button()
