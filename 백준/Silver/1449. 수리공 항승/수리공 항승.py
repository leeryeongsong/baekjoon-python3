n, l = map(int, input().split())
water = list(map(int, input().split()))
cnt = 1
water.sort()
tape = water[0] + l - 1
for i in water:
    if i <= tape:
        continue
    else:
        tape = i + l - 1
        cnt += 1
print(cnt)