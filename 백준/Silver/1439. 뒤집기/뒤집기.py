str = input()
cnt = 0

for i in range(1, len(str)):
    if str[i] != str[i-1]:
        cnt += 1
cnt += 1
cnt = cnt // 2
print(cnt)