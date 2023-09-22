from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.CommonElements as ce


class IdPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
