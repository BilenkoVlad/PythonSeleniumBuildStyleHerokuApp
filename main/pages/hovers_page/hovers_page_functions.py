from main.pages.assertions import Assertions
from main.utils.action_manager.actions_manager import ActionsManager
from main.utils.browser_manager.browser_manager import BrowserManager


class HoversPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _AVATARS = ".//div[@class='figure']"
    _AVATARS_NAMES = ".//div[@class='figcaption']/h5"
    _AVATARS_LINKS = ".//div[@class='figcaption']/a"
    _AVATAR_NAME = ["name: user1", "name: user2", "name: user3"]

    def hover_on_avatars_with_assertion(self):
        assertions = Assertions()
        for i in range(len(BrowserManager().find_elements_by_XPATH(self._AVATARS))):
            ActionsManager().get_actions().move_to_element(
                BrowserManager().find_elements_by_XPATH(self._AVATARS)[i]).perform()
            assertions \
                .the_element_is_displayed(BrowserManager().find_elements_by_XPATH(self._AVATARS_NAMES)[i]) \
                .the_element_is_displayed(BrowserManager().find_elements_by_XPATH(self._AVATARS_LINKS)[i]) \
                .the_element_text_equals(BrowserManager().find_elements_by_XPATH(self._AVATARS_NAMES)[i],
                                         self._AVATAR_NAME[i]) \
                .the_element_text_equals(BrowserManager().find_elements_by_XPATH(self._AVATARS_LINKS)[i],
                                         "View profile")
        return self
