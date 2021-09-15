# https://www.acmicpc.net/problem/10156

snack, count, now_money = map(int, input().split())
total_cost = snack*count

if total_cost > now_money:
    print(total_cost-now_money)
else:
    print(0)
