import sys

n, m = map(int, input().split())
store = []

for _ in range(m):
    store.append(list(map(int, sys.stdin.readline().split())))

min_set = store[0][0]
min_ind = store[0][1]

for i in range(m):
    if min_set > store[i][0]:
        min_set = store[i][0]
    if min_ind > store[i][1]:
        min_ind = store[i][1]

set_n = 0
if n % 6 == 0 :
    set_n = n // 6
else:
    set_n = (n // 6) + 1

only_set = min_set*set_n
set_and_ind = min_set*(n // 6) + min_ind*(n % 6)
only_ind = min_ind*n

print(min(only_set, set_and_ind, only_ind))