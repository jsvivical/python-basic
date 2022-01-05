#1 리스트 순회
for looper in [1,2, 3,4,5]:
    print(looper, end = ",")

#정해진 정수 범위 만큼만 반복
for looper in range(100): # 0 ~ (100 - 1) 까지 반복 : 총 100번
    print(looper, end = ",")
    
print("\n\n")
for looper in range(50, 100, 2) :#10에서 100까지 2칸씩 이동
    print(looper,end = ",")
    if looper == 98 :
        print(looper)
    
#문자열 순회
for looper in 'abcdefg':
    
    if looper == 'g':
        print(looper)
    elif looper == 'e':
        continue
    else:
        print(looper,end = " ")
        
#while 반복문  
i = 0
while i < 100 :
     print(i, end = " ")
     i += 1

print()