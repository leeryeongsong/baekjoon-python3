# https://www.acmicpc.net/problem/19944

N, M = map(int, input().split())

if M == 1 or M == 2:
    print('NEWBIE!')
elif 3 <= M <= N :
    print('OLDBIE!')
else:
    print('TLE!')
