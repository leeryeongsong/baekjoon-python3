t = int(input())
for _ in range(t):
    n = int(input())
    x = 0
    tree = list(map(int, input().split()))
    tree.sort()
    mi = [tree[1]-tree[0], tree[-1]-tree[-2]]
    for i in range(0,len(tree)-2):
        mi.append(tree[i+2]-tree[i])
    print(max(mi))