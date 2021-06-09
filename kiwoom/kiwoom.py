from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        print("Kiwoom() class start")

        ####### event loop를 실행하기 위한 변수 모음
        self.login_event_loop = QEventLoop()  # 로그인 요청용 이벤트 루프

        ####### 초기 셋팅 함수들 바로 실행
        self.get_ocx_instance()         #OCX방식을 파이썬에 사용할 수 있게 변환해 주는 함수
        self.event_slots()               #키움과 연결하기 위한 시그널 / 슬롯 모음
        self.signal_login_commConnect() #로그인 요청 함수 포함


    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()

    def login_slot(self, err_code):
        print(errors(err_code)[1])

        self.login_event_loop.exit()