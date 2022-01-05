# random 모듈
import urllib.request as ur
import time
import random

print(random.randint(0, 100))  # 0 - 100까지의 난수를 출력

# time 모듈
print(time.localtime())

# urllib 모듈
# 웹 주소의 정보를 불러옴
# urllib의 request모듈을 사용하면 특정 url의 정보를 가져올 수 있음.
# urllib.request.urlopen()의 괄호에 특정 웹 주소를 입력하면 해당 주소의 html 정보를 가져옴.

response = ur.urlopen("http://google.com")
print(response.read())
