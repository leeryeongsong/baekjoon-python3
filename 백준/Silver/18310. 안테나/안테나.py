n = int(input())
dis = list(map(int, input().split()))
dis.sort()
print(dis[(n-1) // 2])