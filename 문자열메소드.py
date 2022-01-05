print("len() 함수: 문자열의  문자 개수 반환")
str = "Hello World!"
print(len(str))
print()

print("upper()메소드 : 대문자로 변환")
upper_str = str.upper()
print(upper_str)
print()

print("lower() 메소드 : 소문자로 변환")
lower_str = upper_str.lower()
print(lower_str)
print()

print("title() 메소드 : 각 단어의 앞글자만 대문자로 변환")
title_str = lower_str.title()
print(title_str)
print()

print("capitalize()메소드 : 첫 문자를 대문자로 변환")
cap_str = lower_str.capitalize()
print(cap_str)
print()

print("count(\"찾을 문자열\") 메소드 : '찾을 문자열이 몇 개 들어있는지 개수 반환")
a = str.count("o")
print(a)
print()

print("find(\"찾을 문자열\") 메소드 : \"찾을 문자열\"이 왼쪽 끝부터 시작해서 몇 번째에 있는지 반환")
b = str.find("World!")
print(b)
print()

print("rfind(\"찾을 문자열\") 메소드 : 오른쪽 끝부터 시작해서 몇 번째에 위치하는지 반환")
c = str.find("World!")
print(c)
print()

print("startswith(\"찾을 문자열\")메소드 : 찾을 문자열로 시작하는지 여부 반환")
d = str.startswith("Bye")
print(d)
print()

print("endswith(\"찾을 문자열\") 메소드 : 찾을 문자열로 끝나는지 여부 확인")
e = str.endswith("World!")
print(e)
print()

print("strip() 메소드 : 좌우 공백 삭제")
print("rstrip() 메소드 : 오른쪽 공백 삭제")
print("lstrip() 메소드 : 왼쪽 공백을 삭제")

print("split() 메소드 : 문자열을 공백이나 다른 문자로 나누어 문자열 리스트로 반환")
print(str.split())  # 공백으로 구분
print(str.split("l"))  # l로 구분
print()

print("isdigit() 메소드 : 문자열이 숫자인지 여부 반환")
print(str.isdigit())
print()

print("islower() 메소드 : 문자열이 소문자인지 여부 반환")
print("isupper() 메소드 : 문자열이 대문자인지 여부 반환")
