#raise 문
# raise : 필요할 때 예외를 발생시키는 코드
#raise 예외타입(예외정보)

while True:
    value = input("반환할 정수값을 입력해 주세요 : ")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("정수값을 입력하지 않았습니다.")

    print("정수값으로 반환된 숫자 - ", int(value))
