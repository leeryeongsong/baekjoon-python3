n = int(input())
money = []
tip = 0

for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in range(n):
    money[i] = money[i] - i 
    if money[i] > 0:
        tip += money[i]

print(tip)