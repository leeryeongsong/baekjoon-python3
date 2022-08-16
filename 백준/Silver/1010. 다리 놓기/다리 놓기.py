t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    i = m - n
    temp = 1
    for j in range(i):
        temp = temp * (m - j) / (j + 1)
    print(int(temp))