# 리스트 값에 인덱스를 붙여 출력 : enumerate() 함수

words = "The brown fox jumps over the lazy dog."

for i, v in enumerate(words, start=int(5)):
    print(i, v)

del words
# 리스트값을 병렬로 묶어 출력 : zip()함수
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

for a, b in zip(a, b):
    print(a, b)

# 참고 : iterable 자료형
# string, list, tuple, dict, set, range() 함수객체, 파일, collections
