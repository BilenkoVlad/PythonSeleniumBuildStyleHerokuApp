from main.utils.select_manager.select_manager import SelectManager


class DropdownPageFunctions:
    _HEADER_PAGE = ".//div[@class='example']/h3"
    _DROPDOWN = ".//select[@id='dropdown']"

    def select_by_visible_text(self, web_element, text):
        SelectManager(web_element=web_element).get_select().select_by_visible_text(text)
        return self
