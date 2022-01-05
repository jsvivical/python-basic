print("구구단 몇 단을 계산할까요? (1 ~ 9)")
print("입력 : ", end = "")
num = int(input())
print("구구단 %d단을 계산합니다.\n" % num)

for i in range (1, 10, 1):
    print("%d * %d = %d" % (num, i, num * i) )