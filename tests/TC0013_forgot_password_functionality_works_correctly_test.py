import pytest

from main.pages.forgot_password_page.forgot_password_page import ForgotPasswordPage
from main.utils.generator.generator import Generator
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC0013ForgotPasswordFunctionalityWorksCorrectlyTest(BaseTest):
    forgot_password_page = ForgotPasswordPage()

    def test_forgot_password_functionality_works_correctly(self):
        _EMAIL = Generator().email_generator()

        self.site \
            .click_on_link("Forgot Password")

        self.forgot_password_page \
            .the_page_url_contains("forgot_password") \
            .the_element_text_equals(self.forgot_password_page.HEADERS_PAGE_ELEMENT(), "Forgot Password") \
            .the_element_text_equals(self.forgot_password_page.FIELD_LABEL_ELEMENT(), "E-mail") \
            .the_element_text_equals(self.forgot_password_page.BUTTON_NAME_ELEMENT(), "Retrieve password") \
            .the_element_is_displayed(self.forgot_password_page.EMAIL_FIELD_ELEMENT()) \
            .the_element_is_displayed(self.forgot_password_page.RETRIEVE_PASSWORD_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.forgot_password_page.EMAIL_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.forgot_password_page.RETRIEVE_PASSWORD_BUTTON_ELEMENT()) \
            .send_keys_to_email_field(_EMAIL) \
            .click_on_retrieve_password_button()
