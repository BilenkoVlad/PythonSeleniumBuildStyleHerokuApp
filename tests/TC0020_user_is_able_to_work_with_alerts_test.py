import pytest

from main.pages.java_script_alerts_page.java_script_alerts_page import JavaScriptAlertsPage
from main.utils.browser_manager.browser_manager import BrowserManager
from tests.base_test import BaseTest


@pytest.mark.smoke
class TC0020UserIsAbleToWorkWithAlertsTest(BaseTest):
    java_script_alerts_page = JavaScriptAlertsPage()

    def test_user_is_able_to_work_with_alerts(self):
        _JS_NAMES = ["Click for JS Alert", "Click for JS Confirm", "Click for JS Prompt"]

        self.site \
            .click_on_link("JavaScript Alerts")

        self.java_script_alerts_page \
            .the_page_url_contains("javascript_alerts") \
            .the_element_text_equals(self.java_script_alerts_page.HEADERS_PAGE_ELEMENT(), "JavaScript Alerts") \
            .the_element_text_equals(self.java_script_alerts_page.BODY_TEXT_ELEMENT(),
                                     "Here are some examples of different JavaScript alerts which can be troublesome for automation") \
            .the_elements_are_displayed(self.java_script_alerts_page.JS_BUTTONS_ELEMENTS()) \
            .the_elements_in_list_equal(self.java_script_alerts_page.JS_BUTTONS_ELEMENTS(), _JS_NAMES) \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_TEXT_ELEMENT(), "Result:") \
            .click_on_js_alert() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS Alert")

        BrowserManager().accept_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(),
                                     "You successfully clicked an alert") \
            .click_on_js_confirm() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS Confirm")

        BrowserManager().accept_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(), "You clicked: Ok") \
            .click_on_js_confirm() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS Confirm")

        BrowserManager().dismiss_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(), "You clicked: Cancel") \
            .click_on_js_prompt() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS prompt")

        BrowserManager().send_keys_to_alert("Test text with !@#$%^&*()")
        BrowserManager().accept_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(),
                                     "You entered: Test text with !@#$%^&*()") \
            .click_on_js_prompt() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS prompt")

        BrowserManager().send_keys_to_alert("Test text with !@#$%^&*()")
        BrowserManager().dismiss_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(), "You entered: null") \
            .click_on_js_prompt() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS prompt")

        BrowserManager().accept_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(), "You entered:") \
            .click_on_js_prompt() \
            .the_alert_is_presented() \
            .the_alert_text_equals("I am a JS prompt")

        BrowserManager().dismiss_alert()

        self.java_script_alerts_page \
            .the_element_text_equals(self.java_script_alerts_page.RESULT_MESSAGE_ELEMENT(), "You entered: null")
