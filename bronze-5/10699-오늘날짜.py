# https://www.acmicpc.net/problem/10699
# 오늘의 날짜 정보를 가져오려면, datetime 모듈을 import하면 된다.

import datetime
print(str(datetime.datetime.now())[:10])
#print(datetime.datetime.today().strftime("%Y-%m-%d"))
#print(datetime.datetime.now().strftime("%Y-%m-%d"))
