import sys
t = int(input())
for _ in range(t):
    n = int(input())
    day = list(map(int, sys.stdin.readline().split()))
    money = 0
    max_cost = 0
    for i in range(n-1, -1, -1):
        if(day[i] > max_cost):
            max_cost = day[i]
        else:
            money += max_cost-day[i]
    print(money)