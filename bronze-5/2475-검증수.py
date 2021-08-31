# https://www.acmicpc.net/problem/2475

a, b, c, d, e = map(int, input().split())
sum = a**2 + b**2 + c**2 + d**2 + e**2
num = sum%10
print(num)
