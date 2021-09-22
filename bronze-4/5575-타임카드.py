# https://www.acmicpc.net/problem/5575

import sys

# 3명의 자료에 대해 같은 과정을 진행하므로, for문을 3번 시행한다.
for i in range(3):
# 한 명의 출근 시간(시, 분, 초)과 퇴근 시간(시, 분, 초)을 공백을 기준으로 입력받는다.
    time = list(map(int, sys.stdin.readline().split()))
# 근무 시간 시간, 분, 초 중 '시간'을 구하기 위해 time[3]와 time[0]의 차를 구한다.
    h = time[3] - time[0]
# 근무 시간 시간, 분, 초 중 '분'을 구하기 위해 time[4]와 time[1]의 차를 구하는데, 이 값이 음수이면 시간 h에서 1을 빼고 분 m에 60을 더한다.
    m = time[4] - time[1]
    if m < 0:
        h -= 1
        m += 60
# 근무 시간 시간, 분, 초 중 '초'를 구하기 위해 time[5]와 time[2]의 차를 구하는데, 이 값이 음수이면 분 m에서 1을 빼고 s에 60을 더한다. m이 음수라면, 시간 h에서 1을 빼고 m에 60을 더한다.
    s = time[5] - time[2]
    if s < 0:
        m -= 1
        s += 60
        if m < 0:
            h -= 1
            m += 60    
# 근무 시간 h, m, s를 출력한다.
    print(h, m, s)
