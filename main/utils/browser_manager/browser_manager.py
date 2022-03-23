from selenium.webdriver.common.by import By

from main.utils.browser_manager.chrome_browser import ChromeBrowser
from main.utils.browser_manager.driver import get_driver
from main.utils.browser_manager.microsoft_edge_browser import MicrosoftEdgeBrowser
from main.utils.logger.LoggingMixin import LoggingMixin
from main.utils.settings.settings import get_settings


class BrowserManager:
    _browser = None
    _supported_browsers = {
        'chrome': ChromeBrowser,
        'edge': MicrosoftEdgeBrowser
    }
    logger = LoggingMixin().logger

    def __init__(self, use_selenium_wire: bool = False):
        super(BrowserManager, self).__init__()
        if not BrowserManager._browser:
            settings = get_settings()
            if settings.browser in self._supported_browsers:
                BrowserManager._browser = self._supported_browsers.get(settings.browser)(
                    use_selenium_wire=use_selenium_wire)
            else:
                raise Exception(f"Browser '{settings.browser}' is not supported. "
                                f"Supported list - '{list(self._supported_browsers.keys())}'")

    def find_element_by_XPATH(self, xpath: str):
        self.logger.debug(f"Element with XPATH:xpath was found")
        return get_driver().find_element(By.XPATH, xpath)

    def find_elements_by_XPATH(self, xpath: str):
        self.logger.debug(f"Elements with XPATH:xpath were found")
        return get_driver().find_elements(By.XPATH, xpath)

    def close_browser(self):
        self.logger.debug("Closing the browser")
        get_driver().close()

    def quit_browser(self):
        self.logger.debug("Quiting the browser")
        get_driver().quit()

    def refresh_page(self):
        self.logger.debug("Refreshed the page")
        get_driver().refresh()

    def switch_to_main_page(self):
        self.logger.debug("Switch to default content")
        get_driver().switch_to.default_content()

    def navigate_back_in_page(self):
        self.logger.debug("Navigate back in page")
        get_driver().back()

    def get_current_url(self):
        url = get_driver().current_url
        self.logger.debug(f"Current site URL is '{url}'")
        return url

    def switch_to_frame(self, web_element):
        self.logger.debug("Switch to frame")
        get_driver().switch_to.frame(web_element)

    def switch_to_default_content(self):
        self.logger.debug("Switch to default content")
        get_driver().switch_to.default_content()

    def switch_to_alert(self):
        self.logger.debug("Switch to alert")
        var = get_driver().switch_to.alert
        return var

    def accept_alert(self):
        self.logger.debug("Accept alert")
        get_driver().switch_to.alert.accept()

    def dismiss_alert(self):
        self.logger.debug("Dismiss alert")
        get_driver().switch_to.alert.dismiss()

    def send_keys_to_alert(self, text):
        self.logger.debug(f"Send {text} into alert")
        get_driver().switch_to.alert.send_keys(text)
