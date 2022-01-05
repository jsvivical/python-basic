a = [1, 2, 3, 4, 5]

a.append(10)  # push
print(a)
print(a.pop())  # pop
print(a)
a.append(20)
print(a)

# 스택을 이용해 문자열 역순으로 배치
str = list("PYTHON")
reverse = []
for _ in range(len(str)):
    reverse.append(str.pop())

print(reverse)
