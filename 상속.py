# 오버라이딩 : 부모 클래스를 상속받아 동일한 메소드에 대해 재정의해 사용하는 것을 오버라이딩
# 파이썬에서는 오버로딩이 필요 없음 ,디폴트매개변수 문법이 있음

# def sum(num1, num2) :
#     return num1 + num2
#
#
# print(sum(100,200))
# print(sum("korea","seoul"))


class ProtoTV:
    def __init__(self, isOn, channel, volume):
        self.isOn = isOn
        self.channel = channel
        self.volume = volume

    def set_on(self, isOn):
        self.isOn = isOn

    def set_channel(self, cnl):
        if 0 < cnl < 1000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.volume = vol

    def get_on(self):
        return self.isOn

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume


class TV(ProtoTV) : # ProtoTV 로 부터 상속을 매개변수 처럼 받음
    def set_channel(self, cnl): # 슈퍼클래스가 가진 메소드를 상속받아 재정의
        if 0 < cnl < 2000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")


lg_tv = TV(False, 10, 10)
samsung_tv = TV(False, 20, 20)
samsung_tv.set_channel(1200)

proto = ProtoTV(False, 10, 10)
proto.set_channel(1000)