import time

from behave import *

from base.BasePage import BasePage
from pages.MainPage import MainPage
from pages.IdPage import IdPage
from pages.LivenessPage import LivenessPage
from pages.ResultPage import ResultPage
import pages.CommonElements as ce
import utilities.CustomLogger as cl

class FacesdkTest:

    @given("기초설정 + 앱 진입하기")
    def class_objects(context):
        # bdd
        context.mp = MainPage(context.driver)
        context.bp = BasePage(context.driver)
        context.lv = LivenessPage(context.driver)
        context.ip = IdPage(context.driver)
        context.rp = ResultPage(context.driver)

        # context.driver.close_app()

        # 홈 화면 > 앱 아이콘 선택
        context.bp.find_element_by_xpath(ce.ios_facesdk_app).click()


    @when("신분증 촬영 대기하기 + liveness 촬영")
    def class_objects(context):
        # 신분증 촬영 버튼 클릭
        context.mp.신분증본인확인_버튼().click()

        # 신분증 촬영 화면으로 넘어감 확인 "영역안에 신분증이 꽉 차도록 조절하면 자동으로 촬영됩니다."
        context.bp.is_exist(ce.id_guide_text)

        # liveness 촬영 화면으로 넘어감 확인 "원 안에 얼굴을 위치하세요"
        # context.bp.is_exist(ce.liveness_guide_text)


    @then("결과값 받아오기")
    def class_objects(context):
        # 결과화면에서 결과값 받아오기
        confidence = context.rp.result_confindence().get_attribute("name")
        distance = context.rp.result_distance().get_attribute("name")
        liveness_confidecne = context.rp.result_liveness_confidence().get_attribute("name")
        name = context.rp.result_name().get_attribute("name")
        num = context.rp.result_num().get_attribute("name")

        print("*** confidence : " + confidence)
        print("*** distance : " + distance)
        print("*** liveness_confidence : " + liveness_confidecne)

        print("*** name : " + str(name))
        print("*** num : " + str(num))

        # 메인 화면으로 복귀
        context.bp.find_element_by_xpath(ce.button_arrow).click()
        context.bp.find_element_by_xpath(ce.button_arrow).click()
        context.bp.find_element_by_xpath(ce.button_x).click()


