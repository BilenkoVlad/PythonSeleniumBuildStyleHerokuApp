from random import random


class Generator:
    _SYMBOLS = "abcdefghijklmnopqrstuvxyz0123456789"

    def email_generator(self) -> str:
        email = ""
        for i in range(10):
            index = int(len(self._SYMBOLS) * random())
            email += self._SYMBOLS[index]
        return email + "@mailinator.com"
