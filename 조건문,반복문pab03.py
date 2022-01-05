import random

end = True
number = 0
while end:
    print("임의의 숫자를 생성합니다.")
    rand_num = random.randint(0, 5)
    print("임의의 숫자를 생성하였습니다. 무슨 숫자인지 맞춰주세요 : ", end = "")
    number = int(input())
    if rand_num != number :
        if number == 9999:
            print("게임을 종료합니다.\n")
            break
        else :
            print("틀렸습니다. 정답은 ",rand_num," 이었습니다.")
            print("다시 진행합니다.\n")
    else:
        print("정답입니다. 게임을 종료합니다.\n")
        end = False
