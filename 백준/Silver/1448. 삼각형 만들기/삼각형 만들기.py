import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse = True)
for i in range(n - 2):
    if arr[i] < arr[i+1] + arr[i + 2]:
        print(arr[i] + arr[i + 1] + arr[i + 2])
        quit()
    else:
        continue
print(-1)