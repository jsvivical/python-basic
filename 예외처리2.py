# try-except-else 구문
# try : 예외 발생 가능 코드
# except : 예외 발생 시 실행되는 코드
# else : 에러가 발생하지 않을 때 실행되는 코드

for i in range(10):
    try:
        result = 10 / i
        print(result)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
