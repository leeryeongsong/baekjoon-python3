n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
l = len(arr[0])
temp = arr[0]


for i in range(1, n):
    for j in range(l):
        if temp[j] != "?":
            if arr[i][j] != temp[j]:
                temp[j] = "?"

temp = ''.join(temp)
print(temp)
