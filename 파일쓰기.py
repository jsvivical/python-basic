# 파일쓰기

import os
f = open("count_log.txt", "w", encoding="utf8")
for i in range(1, 11):
    data = "%d번째 줄이다.\n" % i
    f.write(data)
f.close()


# 새로운 글 추가하기
with open("count_log.txt", "a", encoding="utf8") as f:
    for i in range(1, 11):
        data = "%d 번째 줄이다\n" % i
        f.write(data)

# 디렉토리 만들기 (os모듈 사용)
os.mkdir("log")
# 만들었는지 확인하는 코드
if not os.path.isdir("C:\\Users\\jsviv\\OneDrive\\바탕 화면\\파이썬 기본 문법\\log"):
    os.mkdir("log")
