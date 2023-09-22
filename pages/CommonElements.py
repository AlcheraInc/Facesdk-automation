#Common Path
# 화면 좌측 상단 X 버튼
button_x = '//XCUIElementTypeButton[@name="xmark"]'
button_arrow = "//XCUIElementTypeButton[@name='arrow']"

# 홈화면 > Facesdk 앱
ios_facesdk_app = "//XCUIElementTypeIcon[@name='Face SDK Pro Demo']"

# MainPage Path
switch_ssa = '*//XCUIElementTypeSwitch'
button_liveness = '//XCUIElementTypeButton[@name="라이브니스"]'
button_ssa = "//XCUIElementTypeStaticText[@name='신분증 본인 확인']"
button_ssa_id = "//XCUIElementTypeButton[@name='신분증 본인 확인']"

# Id Page
id_guide_text = "//XCUIElementTypeStaticText[@name='영역안에 신분증이 꽉 차도록 조절하면 자동으로 촬영됩니다.']"

# LivenessPage Path
liveness_guide_text = "//XCUIElementTypeStaticText[@name='원 안에 얼굴을 위치하세요']"
text_ssa_auto = '//XCUIElementTypeStaticText[@name="영역안에 신분증이 꽉 차도록 조절하면 자동으로 촬영됩니다."]'
text_ssa_bright = '//XCUIElementTypeStaticText[@name="어두운 배경에서 빛이 반사되지 않게 주의해 주세요."]'
text_liveness = '//XCUIElementTypeStaticText[@name="라이브니스"]'
id_liveness = '라이브니스'

# Result Page
result_confidence = "//XCUIElementTypeStaticText[@name='confidence']/following-sibling::XCUIElementTypeStaticText[1]"
result_distance = "//XCUIElementTypeStaticText[@name='distance']/following-sibling::XCUIElementTypeStaticText[1]"
result_liveness_confidence = "//XCUIElementTypeStaticText[@name='liveness confidence']/following-sibling::XCUIElementTypeStaticText[1]"
result_type = "//XCUIElementTypeStaticText[@name='타입']/following-sibling::XCUIElementTypeStaticText[1]"
result_name = "//XCUIElementTypeStaticText[@name='이름']/following-sibling::XCUIElementTypeStaticText[1]"
result_num = "//XCUIElementTypeStaticText[@name='주민등록번호']/following-sibling::XCUIElementTypeStaticText[1]"
