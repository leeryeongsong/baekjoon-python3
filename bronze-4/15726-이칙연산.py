#https://www.acmicpc.net/problem/15726

# 세 수를 연속해서 받고, 순서가 바뀌지 않는 상황에서, 한 번의 곱셈과 한 번의 나눗셈을 이용하여 계산한 값 두 가지 중 가장 큰 값을 출력해야 한다.
A, B, C = map(int, input().split())

# 가능한 조합은 A*B/C, A/B*C 두 가지이고, max()로 둘 중 가장 큰 값을 출력해야 하며, 정수형으로 출력해야 하므로 int()를 이용한다.
print(int(max(A*B/C, A/B*C)))
