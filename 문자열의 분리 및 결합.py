# 문자열의 분리

example = 'python, java, C'
print(example.split(","))
a, b, c = example.split(",")
b = b.strip()
c = c.strip()
print(a)
print(b)
print(c)

# 문자열의 결합
colors = ["red", "blue", "green", "black"]
result = "".join(colors)  # 구분없이 결합
print(result)

result2 = " ".join(colors)  # 공백으로 구분
print(result2)

result3 = ", ".join(colors)  # 쉼표로 구분
print(result3)
