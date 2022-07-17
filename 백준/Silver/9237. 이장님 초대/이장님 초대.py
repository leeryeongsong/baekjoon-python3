n = int(input())

tree = list(map(int, input().split()))
tree.sort(reverse=True)
num = list(range(1, n+1))
sum = [tree[i] + num[i] for i in range(n)]

max_sum = max(sum)
print(max_sum+1)