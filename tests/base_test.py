import unittest

import pytest

from main.pages.home_page.home_page import HomePage
from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.browser_manager.driver import get_driver, set_driver
from main.utils.constants.constants import Constants
from main.utils.logger.LoggingMixin import LoggingMixin
from main.utils.settings.settings import get_settings, Settings


@pytest.mark.incremental
class BaseTest(unittest.TestCase, LoggingMixin):
    _use_selenium_wire = False

    site: HomePage = None
    browser: BrowserManager = None
    driver = None
    logger = LoggingMixin().logger
    settings: Settings = None
    constants: Constants = Constants()

    @classmethod
    def setup_class(cls) -> None:
        cls.settings = get_settings()
        cls.browser = BrowserManager(use_selenium_wire=cls._use_selenium_wire)
        cls.site = HomePage()
        cls.driver = get_driver()
        cls.driver.get(cls.settings.env_url)
        cls.setup_test()

    @classmethod
    def setup_selenium_wire(cls) -> None:
        # setup selenium wire
        # docs https://pypi.org/project/selenium-wire/
        pass

    @classmethod
    def setup_test(cls) -> None:
        # setup for each test case
        pass

    @classmethod
    def teardown_class(cls) -> None:
        cls.teardown_test()
        get_driver().quit()
        cls.site = None
        cls.browser = None
        BrowserManager._browser = None
        set_driver(None)

    @classmethod
    def teardown_test(cls) -> None:
        # teardown for each test case
        pass
