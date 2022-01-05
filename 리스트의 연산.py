# 합연산
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2)

print(len(color1))

total_color = color1 + color2
print(len(total_color))

# 곱연산(리스트 n번 반복)
color_mul = color1 * 3
print(color_mul)

# in연산 (찾는 요소가 있는지 확인)
print("blue" in color2)
print("blue" in color1)

# 리스트 추가 및 삭제
# append() 메소드 : 리스트 가장 뒤에 요소 추가
for element in dir():
    if element[0: 2] != "__":
        del globals()[element]

print(dir())

color = ['red', 'blue', 'green']
color.append('white')
print(color)
del color

# extend() 메소드: 리스트의 합 연산처럼 리스트를 합치는 기능
color = ['red', 'blue', 'green']
color.extend(['black', 'purple'])
print(color)
del color

# insert() 메소드 : 특정한 위치에 값을 추가할 수 있음.
color = ['red', 'blue', 'green']
color.insert(1, 'orange')
print(color)
del color

# remove() 메소드 : 특정 값을 지우는 기능
color = ['red', 'blue', 'green']
color.remove('red')
print(color)
del color

# 특정 인덱스 값의 변경 , 삭제
color = ['red', 'blue', 'green']
color[0] = 'orange'
print(color)
del color[0]
print(color)
