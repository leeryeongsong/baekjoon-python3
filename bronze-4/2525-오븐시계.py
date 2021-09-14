# https://www.acmicpc.net/problem/2525

now_hour, now_min = map(int, input().split())
cook_min = int(input())
last_hour = now_hour + (now_min + cook_min)//60
if last_hour >= 24:
    last_hour = last_hour-24
last_min = (now_min + cook_min)%60
print(last_hour, last_min)
