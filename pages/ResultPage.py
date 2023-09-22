from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.CommonElements as ce


class ResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def result_confindence(self):
        return BasePage.find_element_by_xpath(self, ce.result_confidence)

    def result_distance(self):
        return BasePage.find_element_by_xpath(self, ce.result_distance)

    def result_liveness_confidence(self):
        return BasePage.find_element_by_xpath(self, ce.result_liveness_confidence)

    def result_type(self):
        return BasePage.find_element_by_xpath(self, ce.result_type)

    def result_name(self):
        return BasePage.find_element_by_xpath(self, ce.result_name)

    def result_num(self):
        return BasePage.find_element_by_xpath(self, ce.result_num)
