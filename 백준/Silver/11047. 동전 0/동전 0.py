n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

num = 0

for i in coin:
    if k // i != 0:
        num += (k // i)
        k -= (k // i) * i
    if k == 0:
        break

print(num)