# https://www.acmicpc.net/problem/5554

sec_sum = 0

# 숫자를 4번 입력받고, 변수 sec_sum에 더하고 저장한다.
for i in range(4):
    sec_part = int(input())
    sec_sum = sec_sum + sec_part

# 이동 시간 중 분을 min에 저장, 초를 sec에 저장한다.
min = sec_sum//60
sec = sec_sum%60
print(min)
print(sec)
