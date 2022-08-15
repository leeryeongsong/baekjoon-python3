n, m = map(int, input().split())
num = list(map(int, input().split()))
for _ in range(m):
    num.sort()
    num[0] = num[1] = num[0] + num[1]
print(sum(num))