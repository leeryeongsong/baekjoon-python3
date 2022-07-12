p = int(input())

p = 1000 - p
num = 0

for i in [500, 100, 50, 10, 5, 1]:
    if p // i != 0:
        num += (p // i)
        p -= (p // i) * i
    if p == 0:
        break

print(num)