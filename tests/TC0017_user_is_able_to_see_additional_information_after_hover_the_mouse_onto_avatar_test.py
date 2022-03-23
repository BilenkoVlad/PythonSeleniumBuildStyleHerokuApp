import pytest

from main.pages.hovers_page.hovers_page import HoversPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0017UserIsAbleToSeeAdditionalInformationAfterHoverTheMouseOntoAvatarTest(BaseTest):
    hovers_page = HoversPage()

    def test_user_is_able_to_see_additional_information_after_hover_the_mouse_onto_avatar(self):
        self.site \
            .click_on_link("Hovers")

        self.hovers_page \
            .the_page_url_contains("hovers") \
            .the_element_text_equals(self.hovers_page.HEADERS_PAGE_ELEMENT(), "Hovers") \
            .the_element_text_equals(self.hovers_page.BODY_TEXT_ELEMENT(),
                                     "Hover over the image for additional information") \
            .the_elements_are_displayed(self.hovers_page.AVATARS_ELEMENTS()) \
            .hover_on_avatars_with_assertion()
