# try - except 구문

for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Not divided by 0")

# 예외의 종류
# IndexError : 범위를 벗어난 인덱스
# NameError : 존재하지 않는 변수 호출
# ZeroDivisionError : 0으로 수를 나눌 때
# ValueError : 변환할 수 없는 문자나 숫자를 변환할 때
# FileNotFoundError : 존재하지 않는 파일을 호출할 때

# 예외 에러 메시지
# 에러를 출력하면 해당하는 메시지가 출력됨

for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError as e:
        print(e)
        print("Not divided by 0")
