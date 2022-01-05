#문법 
# if (조건) : 
#     명령문
#     명령문
# elif (조건) :
#     명령문
#     명령문
# else:
#     명령문
#     명령문

#비교연산자
# x < y
# x > y
# x == y
# x is y : x와 y의 메모리가 같으면 True, 다르면 False
# x is not y : x와 y의 메모리가 다르면 True, 같으면 False
# x >= y
# x <= y
    





student = ['진솔', '주석', '민욱', '진영', '찬주']
id = ['2014034070', '2014034024', '2014050240', '2014034071','2014034075']
score = [40, 50, 50, 70, 60]
underscore = []

print("50점 초과자\n")
i = 0
for i in range(len(student)) :
    if score[i] >= 50 :
        print(id[i]," ", student[i] ," ",score[i])
    else :
        underscore.append(i)
        

print("\n\n")        
print("50점 미만자\n")
        
for i in underscore : 
    print(id[i] , " " , student[i], " " ,score[i])