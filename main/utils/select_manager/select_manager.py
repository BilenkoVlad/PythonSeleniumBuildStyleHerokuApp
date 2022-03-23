from selenium.webdriver.support.select import Select

select = None


class SelectManager:
    _select = None

    def __init__(self, web_element):
        super(SelectManager, self).__init__()
        self.set_select(Select(web_element))

    def set_select(self, new_driver):
        global select
        select = new_driver

    def get_select(self):
        global select
        return select
