import sys

n = 0
t = int(input())
last_y = 0

for _ in range(t):
    n = int(input())
    score = []
    num = 0
    for i in range(n):
        score.append(list(map(int, sys.stdin.readline().split())))
    score.sort(key = lambda x: x[0])

    last_y = score[0][1]

    for [_ , y] in score:
        if y <= last_y:
            num += 1
            last_y = y
            
    print(num)