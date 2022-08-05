s = int(input())
sum = 3
n = 2
if s == 1:
    print(1)
else:
    while sum <= s:
        n += 1
        sum = n*(n+1)/2
    print(n-1)