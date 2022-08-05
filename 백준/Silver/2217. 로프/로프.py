n = int(input())
rope = []
weight = []
num = 1
for _ in range(n):
    rope.append(int(input()))
rope.sort()
while num <= n:
    weight.append(rope[n-num]*num)
    num += 1
print(max(weight))