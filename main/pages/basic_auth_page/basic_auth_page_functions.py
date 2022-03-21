from main.utils.browser_manager.driver import get_driver
from main.utils.logger.LoggingMixin import LoggingMixin
from main.utils.settings.settings import Settings


class BasicAuthPageFunctions(LoggingMixin):
    def login_to_page(self, username, password):
        self.logger.debug(f"Login to page with username: {username} and password: {password}")
        get_driver().get(url=f"https://{username}:{password}@{Settings().env_url.split('//')[1] + '/basic_auth'}")
        return self
