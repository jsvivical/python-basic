# 일반적인 함수
def f(x, y):
    return x + y


print(f(1, 2))

# 람다함수


def f(x, y): return x + y


print(f(1, 4))
print((lambda x, y: x + y)(1, 4))

del f
# 람다합수의 다양한 형태
# 1
def f(x, y): return x + y


f(1, 4)
del f

# 2


def f(x): return x ** 2  # 제곱승 연산자


print(f(3))

# 3
f = lambda x, *args: x + sum(args)
print(f(1, 2, 3, 4, 5))

print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
