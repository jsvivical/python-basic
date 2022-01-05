# 세트 : 값을 순서 없이 저장하면서 중복을 불허하는 자료형
# 수학의 집합과 비슷한 개념
s = set([1, 2, 3, 4, 1, 2, 3])
print(s)

# 세트는 튜플과 달리 값의 삭제나 변경이 가능하다.
print("세트에 값 추가하기(중복된 값은 추가되지 않음")
s.add(1)
print(s)
s.add(5)
print(s)

print("세트에 값 제거하기")
s.remove(1)
s.discard(2)
print(s)

print("리스트 추가하기(중복된 값은 추가되지 않음.")
s.update([1, 2, 3, 4, 5, 6, 7])
print(s)

print("모든 원소 삭제")
s.clear()
print(s)

s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])

print(s1, "\n", s2)
print("합집합")
print(s1 | s2)
unionset = s1.union(s2)
print(unionset)

print("교집합")
print(s1 & s2)
intersection_set = s1.intersection(s2)
print(intersection_set)

print("차집합")
print(s1 - s2)
difference_set = s1.difference(s2)
print(difference_set)
