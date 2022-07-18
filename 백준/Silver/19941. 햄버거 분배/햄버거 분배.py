n, k = map(int, input().split())
str = list(input())
count = 0

for i in range(len(str)):
    if str[i] == "P":
        for j in range(max(i-k, 0), min(i+k+1, len(str))):
            if str[j] == "H":
                count += 1
                str[j] = "O"
                break
print(count)