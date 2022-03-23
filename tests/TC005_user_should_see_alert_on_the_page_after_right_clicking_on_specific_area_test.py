import pytest

from main.pages.context_menu_page.context_menu_page import ContextMenuPage
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC005UserShouldSeeAlertOnThePageAfterRightClickingOnSpecificAreaTest(BaseTest):
    context_menu_page = ContextMenuPage()

    def test_user_should_see_alert_on_the_page_after_right_clicking_on_specific_area(self):
        self.site \
            .click_on_link("Context Menu")

        self.context_menu_page \
            .the_page_url_contains("context_menu") \
            .the_element_text_equals(self.context_menu_page.HEADER_PAGE_ELEMENT(), "Context Menu") \
            .the_element_text_equals(self.context_menu_page.BODY_TEXT_ELEMENTS()[0],
                                     "Context menu items are custom additions that appear in the right-click menu.") \
            .the_element_text_equals(self.context_menu_page.BODY_TEXT_ELEMENTS()[1],
                                     "Right-click in the box below to see one called 'the-internet'. When you click "
                                     "it, it will trigger a JavaScript alert.") \
            .the_element_is_displayed(self.context_menu_page.CONTEXT_BOX_ELEMENT()) \
            .left_click_on_context_box() \
            .the_alert_is_not_presented() \
            .click_on_header() \
            .the_alert_is_not_presented() \
            .right_click_on_context_box()

        BrowserManager().accept_alert()

        self.context_menu_page \
            .the_alert_is_not_presented()
