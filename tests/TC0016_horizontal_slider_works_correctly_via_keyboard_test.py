import pytest

from main.pages.horizontal_slider_page.horizontal_slider_page import HorizontalSliderPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0016HorizontalSliderWorksCorrectlyViaMouseAndKeyboardTest(BaseTest):
    horizontal_slider_page = HorizontalSliderPage()

    def test_horizontal_slider_works_correctly_via_keyboard(self):
        self.site \
            .click_on_link("Horizontal Slider")

        self.horizontal_slider_page \
            .the_page_url_contains("horizontal_slider") \
            .the_element_text_equals(self.horizontal_slider_page.HEADER_TEXT_ELEMENT(), "Horizontal Slider") \
            .the_element_text_equals(self.horizontal_slider_page.BODY_TEXT_ELEMENT(),
                                     "Set the focus on the slider (by clicking on it) and use the arrow keys to move it"
                                     " right and left. Or click and drag the slider with your mouse. It will indicate "
                                     "the value of the slider to the right.") \
            .the_element_is_displayed(self.horizontal_slider_page.SLIDER_ELEMENT()) \
            .the_element_is_enabled(self.horizontal_slider_page.SLIDER_ELEMENT()) \
            .the_element_text_equals(self.horizontal_slider_page.RANGE_NUMBER_ELEMENT(), "0") \
            .move_slider_up_by_keyboard_with_assertion() \
            .move_slider_down_by_keyboard_with_assertion()
