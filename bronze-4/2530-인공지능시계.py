# https://www.acmicpc.net/problem/2530
"""
# 틀렸습니다
now_hour, now_min, now_sec = map(int, input().split())
cook_sec = int(input())
last_sec = (now_sec + cook_sec)%60
last_min = (now_min + (now_sec + cook_sec)//60)%60
last_hour = now_hour + (now_min + (now_sec + cook_sec)//60)//60
if last_hour > 23 :
    last_hour = last_hour - 24 #59이어도 24만 뺀다. 

print(last_hour, last_min, last_sec)
"""

now_hour, now_min, now_sec = map(int, input().split())
cook_sec = int(input())
last_sec = (now_sec + cook_sec)%60
last_min = (now_min + (now_sec + cook_sec)//60)%60
last_hour = (now_hour + (now_min + (now_sec + cook_sec)//60)//60)%24

print(last_hour, last_min, last_sec)
