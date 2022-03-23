class KeyPressesPageFunctions:
    _HEADERS_PAGE = ".//div[@class='example']/h3"
    _BODY_TEXT = ".//div[@class='example']/p"
    _INPUT_FIELD = ".//input[@id='target']"
    _RESULT_TEXT = ".//p[@id='result']"

    def send_keys_to_field(self, web_element, value):
        web_element.send_keys(value)
        return self
