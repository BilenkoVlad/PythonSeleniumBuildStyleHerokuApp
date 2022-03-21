from main.utils.browser_manager.browser_manager import BrowserManager


class HomePageFunctions:

    def click_on_link(self, link_name: str):
        BrowserManager().find_element_by_XPATH(f".//*[contains(text(), '{link_name}')]").click()
        return self
