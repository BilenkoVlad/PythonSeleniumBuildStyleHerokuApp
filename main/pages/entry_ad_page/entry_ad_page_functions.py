from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from main.utils.browser_manager.browser_manager import BrowserManager
from main.utils.browser_manager.driver import get_driver


class EntryAdPageFunctions:
    _MODAL_WINDOW = ".//div[@class='modal']"
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _CLICK_HERE = ".//a[@id='restart-ad']"
    _TITLE = ".//div[@class='modal-title']/h3"
    _TEXT = ".//div[@class='modal-body']/p"
    _CLOSE_BUTTON = ".//div[@class='modal-footer']/p"

    def click_close_button(self):
        BrowserManager().find_element_by_XPATH(self._CLOSE_BUTTON).click()
        return self

    def click_on_click_here(self):
        while not BrowserManager().find_element_by_XPATH(self._MODAL_WINDOW).is_displayed():
            BrowserManager().find_element_by_XPATH(self._CLICK_HERE).click()
            try:
                if WebDriverWait(get_driver(), 3).until(
                        expected_conditions.visibility_of_element_located((By.XPATH, self._MODAL_WINDOW))) is not None:
                    break
            except:
                print("No modal window is presented")
        return self
