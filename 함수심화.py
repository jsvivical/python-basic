# 함수의 호출 방식
#값에 의한 호출 (call by value)
def f(x):
    y = x
    x = 5
    return y * y

x = 3
print(f(x))
print(x)

#참조에 의한 호출
def spam(eggs) : 
    eggs.append(1)
    eggs = [2,3]
    
ham = [0]
spam(ham)
print(ham)
