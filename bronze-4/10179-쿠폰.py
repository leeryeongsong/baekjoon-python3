# https://www.acmicpc.net/problem/10179
# 테스트 케이스의 개수를 입력받아 N에 저장한다.
N = int(input())

# for문을 테스트 케이스 개수만큼 반복한다.
for i in range(N):
# 물건의 할인 전 가격을 입력받고, 0.8을 곱하여, 할인 가격을 price에 저장한다.
    price = float(input())*0.8
# 파이썬 f-string 문자열 포매팅 방식을 사용했다. 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지 나타내기 위해 .2f를 입력했다.
    print(f'${price:.2f}')
