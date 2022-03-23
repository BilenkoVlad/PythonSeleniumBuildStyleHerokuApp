import pytest

from main.pages.form_authentication_page.form_authentication_page import FormAuthenticationPage
from main.pages.form_authentication_page.secure_page.secure_page import SecurePage
from tests.base_test import BaseTest

@pytest.mark.smoke
class TC0014UserIsAbleToLoginTest(BaseTest):
    form_authentication_page = FormAuthenticationPage()
    secure_page = SecurePage()

    def test_user_is_able_to_login(self):
        self.site \
            .click_on_link("Form Authentication")

        self.form_authentication_page \
            .the_page_url_contains("login") \
            .the_element_text_equals(self.form_authentication_page.HEADERS_PAGE_ELEMENT(), "Login Page") \
            .the_element_text_equals(self.form_authentication_page.BODY_TEXT_ELEMENT(),
                                     "This is where you can log into the secure area. Enter tomsmith for the username "
                                     "and SuperSecretPassword! for the password. If the information is wrong you should"
                                     " see error messages.") \
            .the_element_text_equals(self.form_authentication_page.USERNAME_LABEL_ELEMENT(), "Username") \
            .the_element_is_displayed(self.form_authentication_page.USERNAME_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.form_authentication_page.USERNAME_FIELD_ELEMENT()) \
            .the_element_text_equals(self.form_authentication_page.LOGIN_BUTTON_ELEMENT(), "Login") \
            .the_element_is_displayed(self.form_authentication_page.LOGIN_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.form_authentication_page.LOGIN_BUTTON_ELEMENT()) \
            .the_element_text_equals(self.form_authentication_page.PASSWORD_LABEL_ELEMENT(), "Password") \
            .the_element_is_displayed(self.form_authentication_page.PASSWORD_FIELD_ELEMENT()) \
            .the_element_is_enabled(self.form_authentication_page.PASSWORD_FIELD_ELEMENT()) \
            .send_keys_to_field(self.form_authentication_page.USERNAME_FIELD_ELEMENT(), "invalidUsername") \
            .send_keys_to_field(self.form_authentication_page.PASSWORD_FIELD_ELEMENT(), "invalidPassword") \
            .click_login_button() \
            .the_element_is_displayed(self.form_authentication_page.ALERT_ELEMENT()) \
            .the_element_text_equals(self.form_authentication_page.ALERT_ELEMENT(), "Your username is invalid!\n×") \
            .send_keys_to_field(self.form_authentication_page.USERNAME_FIELD_ELEMENT(),
                                self.form_authentication_page.CREDENTIALS_ELEMENTS()[0].text) \
            .send_keys_to_field(self.form_authentication_page.PASSWORD_FIELD_ELEMENT(),
                                self.form_authentication_page.CREDENTIALS_ELEMENTS()[1].text) \
            .click_login_button()

        self.secure_page \
            .the_element_is_displayed(self.secure_page.ALERT_ELEMENT()) \
            .the_element_text_equals(self.secure_page.ALERT_ELEMENT(), "You logged into a secure area!\n×") \
            .the_element_text_equals(self.secure_page.HEADERS_PAGE_ELEMENT(), "Secure Area") \
            .the_element_text_equals(self.secure_page.BODY_TEXT_ELEMENT(),
                                     "Welcome to the Secure Area. When you are done click logout below.") \
            .the_element_text_equals(self.secure_page.LOGOUT_BUTTON_LABEL_ELEMENT(), "Logout") \
            .the_element_is_displayed(self.secure_page.LOGOUT_BUTTON_ELEMENT()) \
            .the_element_is_enabled(self.secure_page.LOGOUT_BUTTON_ELEMENT()) \
            .click_logout_button() \
            .the_element_is_displayed(self.secure_page.ALERT_ELEMENT()) \
            .the_element_text_equals(self.secure_page.ALERT_ELEMENT(), "You logged out of the secure area!\n×")
