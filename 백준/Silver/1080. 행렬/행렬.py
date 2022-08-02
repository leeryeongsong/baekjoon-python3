n, m = map(int, input().split())
matrixA = []
matrixB = []
cnt = 0


def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrixA[i][j] = 1 - matrixA[i][j]

for _ in range(n):
    matrixA.append(list(map(int, input())))
for _ in range(n):
    matrixB.append(list(map(int, input())))

for i in range(n-2):
    for j in range(m-2):
        if matrixA[i][j] != matrixB[i][j]:
            reverse(i, j)
            cnt += 1
        

if matrixA == matrixB:
    print(cnt)
else:
    print(-1)