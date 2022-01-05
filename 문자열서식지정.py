# %서식과 format() 메소드

a, b, c = 1, 2, 3
print("%d %d %d\n" % (a, b, c))
print("{} {} {}\n".format(a, b, c))

# 서식 문자
# %s : 문자열
# %c : 문자 1개
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수

# format() 메소드
age = 40
name = "jinsol"
print("I'm {0}years old. And my name is {1}".format(age, name))

# 패딩 : 여유 공간을 지정하여 글자 배열을 맞추고 소수점 자릿수를 맞추는 기능
print("%10d" % 12)
print("%-10d" % 12)
print("%10.3f" % 5.9832)
print("%-10.2f" % 5.9832)

# format() 메소드의 패딩
print("{0:>10s}".format("apple"))  # 띄어쓰기하면 안됨
print("{0:<10s}".format("apple"))
print("{0:>10.3f}".format(5.29572))
print("{0:<10.3f}".format(6.3937))
