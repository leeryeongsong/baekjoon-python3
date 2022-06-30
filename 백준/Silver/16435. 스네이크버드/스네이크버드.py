n, l = map(int, input().split())
fr = list(map(int, input().split()))

a = 1

while a:
    for i in range(n):
        a = 0
        for j in fr:
            if j <= l:
                l += 1
                fr.remove(j)
                a += 1


print(l)