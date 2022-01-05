str = "helloworld"
print(id('h'))
print(id('e'))
print(id('l'))
print(id('l'))
print(id('o'))
# 메모리 상에 순서대로 저장된 것이 아니라 랜덤한 위치에 저장되고 참조값으로 불러옴.

# 문자열의 인덱싱
print(str[0])
print(str[1])
print(str[2])

# 문자열의 슬라이싱
print(str[4:7])

print(str[::2])

# 문자열의 연산
a = "team"
b = "lab"
print(a + " " + b)

print(a * 2 + " " + b * 2)

# 조건문에서의 활용
if 'a' in a:
    print(a)
else:
    print("not included")
