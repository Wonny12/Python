<<<<<<< HEAD
'''월 4회 스터디 -> 3번 온라인 1번 오프라인
오프라인 모임 날짜를 정해주는 프로그램을 작성

조건1: 랜덤으로 날짜를 뽑아야함
조건2: 월별 날짜는 다음을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

output 예시: 오프라인 스터디 모임 날짜는 매월 x일로 선정 되었습니다'''
from random import *
offline_study_date = (int(randint(4,28)))

print("오프라인 스터디 모임 날짜는 매월", offline_study_date,"일로 선정 되었습니다")


=======
from random import *
offline_study_date = (int(randint(4,28)))

print("Offline study date will be ", offline_study_date)
>>>>>>> 7d796aab9bca6ca9a90cafca6980e3329d882c68
