# https://www.acmicpc.net/problem/5522

import sys
sum = 0

for i in range(5):
    score = int(sys.stdin.readline())
    sum = sum + score

print(sum)
