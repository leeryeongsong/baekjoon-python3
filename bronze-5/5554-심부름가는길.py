# https://www.acmicpc.net/problem/5554

sec_sum = 0

for i in range(4):
    sec_part = int(input())
    sec_sum = sec_sum + sec_part

min = sec_sum//60
sec = sec_sum%60
print(min)
print(sec)
