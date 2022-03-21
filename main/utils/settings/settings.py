import json
import os
from typing import Dict

settings = None


def get_settings():
    global settings
    if not settings:
        settings = Settings()

    return settings


class Settings:
    _settings: dict = {}

    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{path}/settings.json', 'r') as json_file:
            from_file = json.load(json_file)
        Settings._settings.update(from_file)

        self.browser = self._settings.get("browser")
        self.env_url = self._settings.get("env_url")
        self.admin_login = self._settings.get("admin_login")
        self.admin_password = self._settings.get("admin_password")

    @classmethod
    def update_settings(cls, update_settings: Dict[str, str]) -> None:
        cls._settings.update(update_settings)
