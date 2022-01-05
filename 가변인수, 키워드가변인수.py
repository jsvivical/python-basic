# *의 패킹기능

def asterisk_test(a, *args):
    print(args)


asterisk_test(1, 2, 3, 4, 5, 6)

del asterisk_test

# *의 언패킹기능


def asterisk_test(a, args):
    print(a, *args)  # 단, args는 튜플자료형이어야 함.
    print(type(args))


asterisk_test(1, (2, 3, 4, 5, 6))


# 마찬가지로 딕셔너리 자료형은 **로 패킹, 언패킹 가능
