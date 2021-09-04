# https://www.acmicpc.net/problem/2845

import sys

L, P = map(int, sys.stdin.readline().split())
sum = L*P
news = [int(x)-sum for x in sys.stdin.readline().split()]
for i in range(5):
    print(news[i], end=' ')
