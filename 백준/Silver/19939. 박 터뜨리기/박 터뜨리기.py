n, k = map(int, input().split())
ans = -1
t = k * (k+1) / 2

if n >= t:
    if (n - t) % k == 0:
        ans = k - 1
    else:
        ans = k

print(ans)