# 일반적인 반복문 + 리스트
result = []
for i in range(10):
    result.append(i)

print(result)
del result

# 리스트 컴프리헨션
result = [i * 2 for i in range(10)]
print(result)

del result

# 리스트 컴프리헨션 용법
# 1 필터링
# 일반적인 반복문
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)

print(result)
del result
# 리스트 컴프리헨션 사용
result = [i for i in range(10) if i % 2 == 0]
print(result)
del result

# if else : 순서 중요
result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)
del result


# 2 중첩반복문
word1 = "hello"
word2 = "world"

result = [i + j for i in word1 for j in word2]
print(result)
del word1, word2, result
# 중첩 + 필터링
case1 = ["a", "b", "c"]
case2 = ["d", "e", "a"]
result = [i + j if i == j else "error" for i in case1 for j in case2]
print(result)
del case1, case2, result

# 이차원 리스트
words = ("the quick brown fox jumps over the lazy dog.".capitalize()).split(" ")
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)
