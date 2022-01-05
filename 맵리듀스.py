# 빅데이터를 처리하기 위한 기본적인 알고리즘

# map()함수 : 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 유용
# 일반적으로 리스트나 튜플처럼 요소가 있는 시퀀스 자료형에 사용
# map(함수이름, 리스트데이터)
from functools import reduce
ex = [1, 2, 3, 4, 5]
def f(x): return x ** 2


print(list(map(f, ex)))
del ex, f
# 한 개 이상의 시퀀스 자료형 데이터의 처리
ex = [1, 2, 3, 4, 5]
def f(x, y): return x + y


print(list(map(f, ex, ex)))


# reduce()함수 : 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
