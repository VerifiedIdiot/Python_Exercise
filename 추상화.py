# 추상화
# 부모 클래스에서 선언한 메소드에 대해서 반드시 상속 받은 클래스에서 기능을 구현 해야 하는 특성
# 추상 메서드가 포함된 부모 클래스는 객체로 만들 수 없고 단지 상속을 주기 위해서만 존재


from abc import *
class NetworkAdapter(metaclass=ABCMeta):    # 추상 클래스 선언
    @abstractmethod
    def connect(self):
        pass    # 구현 할 내용이 없는 경우 pass 키워드를 사용


class LAN(NetworkAdapter):
    def __init__(self, company):    # 생성자 만들기
        self.company = company

    def connect(self):  # 부모에게서 상속 받은 추상 메서드를 구현 함
        print(f"{self.company} LAN에 연결 했습니다.")


class WiFi(NetworkAdapter):
    def __init__(self, company):    # 생성자 만들기
        self.company = company

    def connect(self):  # 부모에게서 상속 받은 추상 메서드를 구현 함
        print(f"{self.company} Wi-Fi에 연결 했습니다.")


class LTE(NetworkAdapter):
    def __init__(self, company):    # 생성자 만들기
        self.company = company

    def connect(self):  # 부모에게서 상속 받은 추상 메서드를 구현 함
        print(f"{self.company} LTE에 연결 했습니다.")


net = input("연결할 네트워크를 선택 [1]LAN, [2]Wi-Fi, [3]LTE : ")
if net == "1":
    adapter = LAN("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = WiFi("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("LG U+")
    adapter.connect()
else:
    print("연결할 네트워크가 없습니다.")
