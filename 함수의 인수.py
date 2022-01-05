# 키워드 인수
def print_something(myname, yourname):
    print("Hello {0}, my name is {1}".format(yourname, myname))


print_something("Park Jinsol", " Python")
print_something(myname="Park jinsol", yourname="python")
del print_something

# 디폴트 인수


def print_something(myname, yourname="Python"):
    print("Hello {0}, my name is {1}".format(myname, yourname))


print_something("Jinsol", "Java")
print_something("Jinsol")

# 가변인수 (* : asterisk로 표현함.)
# 가변인수는 반드시 일반적인 키워드 인수가 끝난 후 넣어야 한다.
# 가변인수는 튜플형태이므로 args[0], args[1]의 식으로 접근가능


def asterisk_test(a, b, *args):
    return a + b + sum(args)


print(asterisk_test(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 가변인수 연습


def asterisk2(*args):
    x, y, *z = args  # args[0] = x, args[1] = y, 그 이후로는 z 튜플에 저장.
    return x, y, z


print(asterisk2(1, 2, 3, 4, 5))

# 키워드 가변 인수
# 저장된 값은 튜플 형태가 아니라 딕셔너리 자료형임.
# 즉 이름과 값이 같이 저장된 형태


def kwargs_test(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second Value is {second}".format(**kwargs))
    print("Third Value is {third}".format(**kwargs))


kwargs_test(first=3, second=4, third=5)
