#변수 메모리 정리
# print(dir())
# for element in dir():
#     if element[0:2] != "__": #문자열 처음부터 2번째까지 __가 아니면
#         del globals()[element]

# print(dir())


#인덱싱
colors = ['red','blue','green']
print(colors[0])
print(len(colors))

#슬라이싱 
city = ['서울', '부산', '인천', '대구','광주', '울산', '수원']
print(city[0 : 3]) # 0번부터 (3 - 1)번까지
print(city[2 : 5])

print(city[ : 5]) # 처음부터 (5 - 1)까지
print(city[2 : ]) #2번부터 끝까지
print(city[:]) #처음부터 끝까지
#리버스 인덱스 
cities = city
print(cities[-8 : ])

#증가값 step
c1 = city[::2] #2칸 단위로 (0, 2, 4번 순)
print(c1)

#역으로 슬라이싱
c2 = city[::-1]
print(c2)
c3 = city[::-2] #거꾸로 2칸 단위
print(c3)

#변수 메모리 정리
# print(dir())
# for element in dir():
#     if element[0:2] != "__": #문자열 처음부터 2번째까지 __가 아니면
#         del globals()[element]

print(dir())

for element in dir():
    if element[0:2] != "__" :
        del globals()[element]
        
print(dir())