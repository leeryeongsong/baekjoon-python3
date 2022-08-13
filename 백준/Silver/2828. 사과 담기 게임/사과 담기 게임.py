n, m = map(int, input().split())
j = int(input())
cnt = 0
left = 1
right = 1 + m - 1
for _ in range(j):
    i = int(input())
    if left <= i <= right:
        continue
    elif i < left:
        cnt += (left - i)
        right -= (left - i)
        left -= (left - i)
    else:
        cnt += (i - right)
        left += (i - right)
        right += (i - right)
print(cnt)