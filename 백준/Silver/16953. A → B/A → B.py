a, b = map(int, input().split())
cnt = 0
while a < b:
    if b % 10 == 1:
        b = b // 10
    else:
        b = b / 2
    cnt += 1
if a == b:
    print(cnt+1)
else:
    print(-1)