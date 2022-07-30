n = int(input())
peo = list(map(int, input().split()))
peo.sort(reverse=True)
sum = 0

for i in range(n):
    sum += peo[i] * (i + 1)
print(sum)