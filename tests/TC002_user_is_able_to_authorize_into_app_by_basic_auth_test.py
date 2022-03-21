import pytest

from main.pages.basic_auth_page.authorized_page import AuthorizedPage
from main.pages.basic_auth_page.basic_auth_page import BasicAuthPage
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC002UserIsAbleToAuthorizeIntoAppByBasicAuthTest(BaseTest):
    basic_auth_page = BasicAuthPage()
    authorized_page = AuthorizedPage()

    def test_TC002_user_is_able_to_authorize_into_app_by_basic_auth(self):
        user_name = "admin"
        password = "admin"
        self.site \
            .click_on_link("Basic Auth")

        self.basic_auth_page \
            .the_page_url_contains("basic_auth") \
            .login_to_page(username=user_name, password=password)

        self.authorized_page \
            .the_page_url_contains(f"https://{user_name}:{password}@the-internet.herokuapp.com/basic_auth") \
            .the_element_text_equals(self.authorized_page.PAGE_NAME_ELEMENT(), "Basic Auth") \
            .the_element_text_equals(self.authorized_page.PAGE_BODY_ELEMENT(),
                                     "Congratulations! You must have the proper credentials.")
