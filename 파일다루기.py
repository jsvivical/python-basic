# 파일읽기
f = open("dream.txt", "r")
str = f.read()
print(str)
f.close()
del f

# with문과 함께 사용
# close() 메소드를 호출하지 않아도 되는 장점이 있음.
with open("dream.txt", "r") as f:
    contents = f.read()
    print(type(contents), contents)

# 한 줄씩 읽어 리스트형으로 반환
with open("dream.txt", "r") as f:
    content_list = f.readlines()
    print(type(content_list))
    print(content_list)

del contents, content_list


# 실행할 때마다 한 줄씩 읽어오기
with open("dream.txt", "r") as f:
    content = f.readline()
    print(type(content))
    print(content)

del content

# 파일 안 글자의 통계정보 출력하기
with open("dream.txt", "r") as f:
    content = f.read()
    word_list = content.split(" ")  # 띄어쓰기로 나누기
    line_list = content.split("\n")  # 개행문자로 나누기

print("총 글자의 수 : %d" % len(content))
print("총 단어의 수 : %d" % len(word_list))
print("총 줄의 수 : %d" % len(line_list))
