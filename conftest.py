from typing import Dict, Tuple

import allure
import pytest
from allure_commons.types import AttachmentType

from main.utils.browser_manager.browsers import Browsers
from main.utils.browser_manager.driver import get_driver
from main.utils.logger.LoggingMixin import LoggingMixin
from main.utils.settings.envs import Environments
from main.utils.settings.settings import Settings


def pytest_sessionstart(session):
    logger = LoggingMixin().logger
    logger.debug("Global one-time session setup")


def pytest_sessionfinish(session, exitstatus):
    logger = LoggingMixin().logger
    logger.debug("Global one-time session teardown")


def pytest_addoption(parser):
    parser.addoption("--env_url", default=Environments.HOME_URL, help="Environment URL")
    parser.addoption("--browser", default=Browsers.CHROME, help="Browser type")


options: Dict[str, str] = {}


def pytest_configure(config):
    global options
    options["env_url"] = config.getoption("env_url")
    options["browser"] = config.getoption("browser")
    Settings.update_settings(options)


_test_failed_incremental: Dict[str, Dict[Tuple[int, ...], str]] = {}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    if "incremental" in item.keywords:
        # incremental marker is used
        if call.excinfo is not None:
            # the test has failed
            # retrieve the class name of the test
            cls_name = str(item.cls)
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the test function
            test_name = item.originalname or item.name
            # store in _test_failed_incremental the original name of the failed test
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(parametrize_index, test_name)

    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = get_driver()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        # retrieve the class name of the test
        cls_name = str(item.cls)
        # check if a previous test has failed for this class
        if cls_name in _test_failed_incremental:
            # retrieve the index of the test (if parametrize is used in combination with incremental)
            parametrize_index = (
                tuple(item.callspec.indices.values())
                if hasattr(item, "callspec")
                else ()
            )
            # retrieve the name of the first test function to fail for this class name and index
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            # if name found, test has failed for the combination of class name & test name
            if test_name is not None:
                pytest.xfail("previous test failed ({})".format(test_name))
