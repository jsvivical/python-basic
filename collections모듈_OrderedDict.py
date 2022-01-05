from collections import OrderedDict

# 그냥 딕셔너리 자료형
d = {}
d['h'] = 100
d['e'] = 2500
d['l'] = 300
d['0'] = 42

for k, v in d.items():  # k는 key, v는 value
    print(k, v)

del d
# OrderedDict 모듈 : key의 순서를 보장함.
d = OrderedDict()
d['h'] = 100
d['e'] = 2500
d['l'] = 32
d['o'] = 400

for k, v in d.items():
    print(k, v)

# OrderedDict가 필요한 경우
#
# 딕셔너리로 데이터 처리 시 key나 value로 데이터를 정렬할 때.
# 예시


def sort_by_key(t):
    return t[0]  # 0은 키으로 정렬, 1은  value로 정렬


for k, v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v)

# sorted 함수 사용법
# sorted(정렬할 데이터)

# sorted(정렬할 데이터, reverse 파라미터)

# sorted(정렬할 데이터, key 파라미터) #key 파라미터는 리스트를 줘야 함.

# sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
