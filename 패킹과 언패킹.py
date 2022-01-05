#패킹 : 한 변수에 여러 데이터를 할당하는 것
#하나의 변수에 든 여러 데이터를 여러 변수에 할당하는 것

t = [1,2,3] #1,2,3을 t에 패킹
 
a, b, c = t #t에 있는 값들을 변수 a,b,c에 언패킹

print(t, a,b,c)

for element in dir():
    if element[0 : 2] != "__" :
        del globals()[element] 
