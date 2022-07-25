import sys

n = int(input())
rank = []
sum = 0
t = 0
for _ in range(n):
    rank.append(int(sys.stdin.readline()))
rank.sort()

for i in range(n):
    t = i + 1 - rank[i]
    if t > 0:
        sum += t
    else:
        sum -= t
print(sum)