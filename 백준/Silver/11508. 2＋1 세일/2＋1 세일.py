import sys
n = int(input())
sum = 0
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
for i in range(n):
    if i % 3 == 2:
        continue
    sum += arr[i]
print(sum)