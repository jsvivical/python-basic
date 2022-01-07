# assert문
# assert : 예외 정보가 조건을 만족하지 않을 경우 예외를 발생시킴.
# assert 예외조건

def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int) #false이면 예외발생
    return bin(decimal_number)


print(get_binary_number(10))
print(get_binary_number("10"))
