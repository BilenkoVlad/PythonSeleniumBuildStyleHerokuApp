from main.utils.logger.LoggingMixin import LoggingMixin


class AuthorizedPageFunctions(LoggingMixin):
    _PAGE_NAME_TEXT = ".//div[@class='example']/h3"
    _PAGE_BODY_TEXT = ".//div[@class='example']/p"
