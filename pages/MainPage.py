from base.BasePage import BasePage
import utilities.CustomLogger as cl
import pages.CommonElements as ce


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def 신분증본인확인_버튼(self):
        return BasePage.find_element_by_xpath(self, ce.button_ssa_id)

    def click_main_form_liveness_button(self):
        BasePage.find_element_by_xpath(self, ce.button_liveness)
        cl.allure_logs("클릭 라이브니스 버튼")

    def click_main_form_ssa_switch(self):
        BasePage.click_elements_by_xpath(self, ce.switch_ssa)
        cl.allure_logs("클릭 SSA 스위치")
