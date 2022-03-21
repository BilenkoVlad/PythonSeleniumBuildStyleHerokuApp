import logging


class LoggingMixin:

    def __init__(self):
        self._logger = logging.getLogger('taf_logger')
        self._logger.setLevel(logging.DEBUG)

    @property
    def logger(self):
        return self._logger
