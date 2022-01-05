from collections import deque

# deque는 스택과 큐를 모두 지원하는 모듈

deque_list = deque()  # deque 생성자

# 스택처럼 값 추가
for i in range(5):
    deque_list.append(i)  # 가장 뒤에 값이 추가됨

    print(deque_list)

# 스택 pop() 메소드
deque_list.pop()
deque_list.pop()
print(deque_list)  # 가장 뒤에 들어온 요소부터 나감.(스택의 성질)
deque_list.clear()

# 큐처럼 사용하려면 appendleft()로 값 추가해야함.
for i in range(10):
    deque_list.appendleft(i)

print(deque_list)

# 큐처럼 값 제거
deque_list.pop()
deque_list.pop()
print(deque_list)

# rotate() 메소드 : 인덱스를 회전시키는 메소드 -> 원형 큐처럼 이루어져있기 때문에 가능
deque_list.rotate(2)
print(deque_list)

# extend() 메소드 : 리스트를 통째로 추가하는 메소드
deque_list.extendleft([10, 11, 12])
print(deque_list)

# deque모듈은 메모리의 효율적 사용과 빠른 속도라는 측면에서 유용
# 대용량으 큐나 스택은 deque 사용 권장
