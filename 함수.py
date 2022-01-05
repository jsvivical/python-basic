# 함수의 선언
# 함수 이름 규칙
# 1 소문자
# 2 띄어쓰기는 언더바(_) 사용
# 3 동사와 명사를 같이 사용하는 경우가 많음.
# 4 외부에 공개하는 함수는 줄임말을 쓰지 않고 짧고 명료한 이름 사용

def calculate_rectangle_area(x, y):
    return x * y


rectangle_x = 10
rectangle_y = 20

print("사각형의 넓이 : %d" % calculate_rectangle_area(rectangle_x, rectangle_y))
