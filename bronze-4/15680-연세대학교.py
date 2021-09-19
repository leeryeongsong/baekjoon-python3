# https://www.acmicpc.net/problem/15680
# 숫자를 입력받아 N에 저장한다.
N = int(input())

# N에 저장된 수가 0이면, YONSEI를 출력하고
# N에 저장된 수가 1이면, Leading the Way to the Future를 출력한다.
if N == 0:
    print("YONSEI")
elif N == 1:
    print("Leading the Way to the Future")
