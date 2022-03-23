import pytest

from main.pages.disappearing_elements_page.disappearing_elements_page import DisappearingElementsPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC006VerifyingThatHiddenItemCanBeShownAfterPollingThePageTest(BaseTest):
    disappearing_elements_page = DisappearingElementsPage()

    def test_verifying_that_hidden_item_can_be_shown_after_polling_the_page(self):
        _BUTTON_NAMES = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]

        self.site \
            .click_on_link("Disappearing Elements")

        self.disappearing_elements_page \
            .the_page_url_contains("disappearing_elements") \
            .the_element_text_equals(self.disappearing_elements_page.HEADER_PAGE_ELEMENT(), "Disappearing Elements") \
            .the_element_text_equals(self.disappearing_elements_page.BODY_TEXT_ELEMENT(),
                                     "This example demonstrates when elements on a page change by "
                                     "disappearing/reappearing on each page load.") \
            .the_elements_are_displayed(self.disappearing_elements_page.BUTTON_ELEMENTS()) \
            .the_elements_in_list_equal(self.disappearing_elements_page.BUTTON_ELEMENTS(), _BUTTON_NAMES) \
            .the_polling_condition(lambda: len(self.disappearing_elements_page.BUTTON_ELEMENTS()) == 5) \
            .the_element_is_displayed(self.disappearing_elements_page.HIDDEN_BUTTON_ELEMENT()) \
            .the_polling_condition(lambda: len(self.disappearing_elements_page.BUTTON_ELEMENTS()) == 4) \
            .the_element_is_not_displayed(self.disappearing_elements_page.HIDDEN_BUTTON_XPATH())
