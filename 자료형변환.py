# 자료형 변환
# 정수 -> 실수
a = 10
print(a)

a = float(10)
print(a)

# 실수 -> 정수
b = 10.6
print(b)

b = int(b)
print(b)


# 문자형 -> 숫자형
a = '76.3'
b = float(a)
print(a)
print(b)

a = float(a)
b = a
print(a + b)

# 숫자형 -> 문자형
a = str(a)
b = str(b)
print(a + b)


print(a, b)
# 자료형 확인
a = int(10.3)
b = float(10.3)
c = str(10.3)

print(type(a))
print(type(b))
print(type(c))

print(dir())
for element in dir():
    if element[0:2] != "__":
        del globals()[element]

print(dir())
print(a)
