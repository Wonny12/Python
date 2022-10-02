from random import *

'''print(random())         #   0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)    #   0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))    #   0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))'''
print(int(random() * 10) + 1)   #   1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45))   # 로또 번호
print(int(randrange(1, 46))) # 1 부터 46 미만의 임의의 값 생성
print(int(randint(1,45))) # 1부터 45이하의 임의의 값 생성