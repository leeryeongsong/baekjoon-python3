# https://www.acmicpc.net/problem/17362

# 답의 규칙성을 살펴보면, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1 ... 인데, 8개 단위로 출력할 값이 반복된다. 그 반복되는 숫자는 ans에 저장한 숫자와 같다.
ans = [1, 2, 3, 4, 5, 4, 3, 2]

# 숫자 n을 입력받아 정수형으로 바꾸고 저장한다.
n = int(input())
# 숫자 n을 8로 나눈 나머지를 remainder에 저장한다.
remainder = n%8
# 리스트 ans의 인덱스 remainder-1 에 해당하는 값이 정답이다.
print(ans[remainder-1])
