from selenium.webdriver import ActionChains

from main.utils.browser_manager.driver import get_driver

actions = None


class ActionsManager:
    _actions = None

    def __init__(self):
        super(ActionsManager, self).__init__()
        self.set_actions(ActionChains(get_driver()))

    def set_actions(self, new_driver):
        global actions
        actions = new_driver

    def get_actions(self):
        global actions
        return actions
