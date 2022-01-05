# 클래스 이름 규칙 첫자는 띄어쓰기 하지않고 단어 첫자는 대문자.
# 카멜케이스

class SoccerPlayer(object):
    # 클래스의 속성을 추가하는 선언.
    # 클래스의 속성에 대한 정보를 선언하기 위해서는 __init__()이라는 예약함수 사용
    # 예약함수(__init__, __str__,__add__ ...)
    # __init__()함수의 첫번째 매개변수는 무조건 self가 되어야함.
    def __init__(self, name, position, back_number):  # self는 자바나 c++의 this와 같은 용법
        self.name = name
        self.position = position
        self.back_number = back_number

    def get_name(self): return self.name
    def get_position(self): return self.position
    def get_back_number(self): return self.back_number

    def print_information(self):
        print("%d번 %s선수는 %s이다." % (self.back_number, self.name, self.position))

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_back_number(self, back_number):
        self.back_number = back_number


ronaldo = SoccerPlayer("Ronaldo", "WB", 23)

ronaldo.print_information()
