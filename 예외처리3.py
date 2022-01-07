# try- except - finally
# finally : 예외 발생 여부와 상관없이 실행되는 코드
try:
    for i in range(10):
        result = 10 / i
        print(result)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Exit")
