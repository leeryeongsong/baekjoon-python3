# https://www.acmicpc.net/problem/16486
# 운동장 트랙의 직선 거리를 입력받아 d1에 저장한다.
d1 = int(input())
# 운동장 트랙 중 반원의 반지름의 길이를 입력받아 d2에 저장한다.
d2 = int(input())

# 운동장의 트랙 전체 길이를 구한다. 직선 거리는 2를 곱하고, 반원의 반지름에는 2와 파이를 곱해서 원의 둘레를 구한 다음, 직선거리*2와 합한다.
# 소수점 6번째 자리까지 표시하기 위해 문자열 포매팅 format()과, 0.6f를 이용했다.
print("{0:0.6f}".format(d1*2+2*d2*3.141592))
