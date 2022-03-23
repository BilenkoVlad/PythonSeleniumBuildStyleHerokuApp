import pytest
from selenium.webdriver.common.keys import Keys

from main.pages.inputs_page.inputs_page import InputsPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0018UserIsAbleToEnterNumberInTheFieldTest(BaseTest):
    inputs_page = InputsPage()

    def test_user_is_able_to_enter_number_in_the_field(self):
        self.site \
            .click_on_link("Inputs")

        self.inputs_page \
            .the_page_url_contains("inputs") \
            .the_element_text_equals(self.inputs_page.HEADERS_PAGE_ELEMENT(), "Inputs") \
            .the_element_text_equals(self.inputs_page.BODY_TEXT_ELEMENT(), "Number") \
            .the_text_equals(self.inputs_page.INPUT_FIELD_ELEMENT().get_attribute("type"), "number") \
            .the_element_is_displayed(self.inputs_page.INPUT_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.inputs_page.INPUT_FIELD_ELEMENT()) \
            .send_keys_to_input_field("any test chars") \
            .clear_input_field() \
            .send_keys_to_input_field("eee") \
            .clear_input_field() \
            .send_keys_to_input_field("123") \
            .clear_input_field() \
            .send_keys_to_input_field("4561e4641") \
            .clear_input_field() \
            .click_on_input_field()

        for i in range(50):
            self.inputs_page \
                .send_keys_to_input_field(Keys.ARROW_UP)

        self.inputs_page \
            .clear_input_field()

        for i in range(50):
            self.inputs_page \
                .send_keys_to_input_field(Keys.ARROW_DOWN)
