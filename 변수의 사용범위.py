def test(t):
    print(x)
    t = 20
    print("In function : %d" % t)


x = 10
test(x)
print("In main : %d" % x)
#print("in main : %d" % t)

# 전역변수


def f():
    global s
    s = "I love London"
    print(s)


s = "I love Paris"
f()
print(s)
