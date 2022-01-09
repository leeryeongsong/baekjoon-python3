#https://www.acmicpc.net/problem/14470

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

#해동 시간 time 변수 선언 후 0 값 저장
time = 0

# 시작 온도 A가 음수라면
if A<0:
# A에서 0도로, (-A)도 만큼 온도 올리고 해동할 때 걸리는 시간 = (-A)*(얼어있는 고기 섭씨 1도 올릴 때 걸리는 시간C) + 해동 시간D
    time = -A*C + D
    A = 0

# 상온 B도로 온도 높일 때 걸리는 시간 = (B-A)*(얼어있지 않은 고기 섭씨 1도 올릴 때 걸리는 시간E)
time = time + (B-A)*E

# time 출력
print(time)
