from selenium.webdriver.chrome.webdriver import WebDriver

driver = None


def set_driver(new_driver):
    global driver
    driver = new_driver


def get_driver() -> WebDriver:
    global driver
    return driver
