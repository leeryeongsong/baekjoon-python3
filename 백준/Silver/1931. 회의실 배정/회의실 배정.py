import sys

n = int(input())
time = []
end = 0
num = 0

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key = lambda x: (x[1], x[0]))

for x, y in time:
    if x >= end:
        num += 1
        end = y

print(num)