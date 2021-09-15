# https://www.acmicpc.net/problem/2480

dice = list(map(int, input().split()))
same = 0

for i in dice:
    if dice.count(i) == 3:
        same = i
        print(10000+i*1000)
        break
    elif dice.count(i) == 2:
        same = i
        print(1000+i*100)
        break

if same == 0:
    print(max(dice)*100)
