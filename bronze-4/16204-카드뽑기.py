# https://www.acmicpc.net/problem/16204

N, M, K = map(int, input().split())
num = N - abs(M-K)
print(num)
