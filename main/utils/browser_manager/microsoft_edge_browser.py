from msedge.selenium_tools.options import Options
from msedge.selenium_tools.webdriver import WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main.utils.browser_manager.driver import get_driver, set_driver
from main.utils.logger.LoggingMixin import LoggingMixin


class MicrosoftEdgeBrowser(LoggingMixin):

    def __init__(self, use_selenium_wire: bool = False, setup_selenium_wire: 'Callable' = None):
        super(MicrosoftEdgeBrowser, self).__init__()
        if not get_driver():
            self._init_browser(use_selenium_wire=use_selenium_wire, setup_selenium_wire=setup_selenium_wire)

    def _init_browser(self, use_selenium_wire: bool = False, setup_selenium_wire: 'Callable' = None):
        options = self._get_options()
        if use_selenium_wire:
            from seleniumwire.webdriver import Edge
            driver = Edge(executable_path=EdgeChromiumDriverManager().install(),
                          options=options)
            setup_selenium_wire()
        else:
            driver = WebDriver(executable_path=EdgeChromiumDriverManager().install(),
                               options=options)
        driver.implicitly_wait(0)
        set_driver(driver)

    def _get_options(self):
        options = Options()

        options.use_chromium = True
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-file-access-from-files")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--allow-cross-origin-auth-prompt")
        options.add_argument("--allow-file-access")
        options.add_argument("--ignore-certificate-errors")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }

        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        return options
