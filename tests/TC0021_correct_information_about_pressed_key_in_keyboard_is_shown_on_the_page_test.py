import pytest
from selenium.webdriver.common.keys import Keys

from main.pages.key_presses_page.key_presses_page import KeyPressesPage
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC0021CorrectInformationAboutPressedKeyInKeyboardIsShownOnThePageTest(BaseTest):
    key_presses_page = KeyPressesPage()

    def test_correct_information_about_pressed_key_in_keyboard_is_shown_on_the_page(self):
        self.site \
            .click_on_link("Key Presses")

        self.key_presses_page \
            .the_page_url_contains("key_presses") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.ARROW_UP) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: UP") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.ARROW_DOWN) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: DOWN") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.ARROW_LEFT) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: LEFT") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.ARROW_RIGHT) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: RIGHT") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.CONTROL) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: CONTROL") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.SHIFT) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: SHIFT") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.TAB) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: TAB") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), Keys.ESCAPE) \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: ESCAPE") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), "a") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: A") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), "q") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: Q") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), "c") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: C") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), ",") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: COMMA") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), "/") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: SLASH") \
            .send_keys_to_field(self.key_presses_page.INPUT_FIELD_ELEMENT(), "[") \
            .the_element_is_displayed(self.key_presses_page.RESULT_TEXT_ELEMENT()) \
            .the_element_text_equals(self.key_presses_page.RESULT_TEXT_ELEMENT(), "You entered: OPEN_BRACKET")
