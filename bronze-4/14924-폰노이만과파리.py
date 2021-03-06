# https://www.acmicpc.net/problem/14924
# 기차의 속도, 파리(fly)의 속도, 두 기차 사이의 거리를 순서대로 공백을 기준으로 입력받아 S,T,D에 각각 저장한다. 
S, T, D = map(int, input().split())
# 파리의 이동 거리를 출력해야 한다.
# 파리의 이동 거리 = (파리의 이동 시간)*(파리의 속도)
# 파리의 이동 거리 = (기차의 이동 시간)*(파리의 속도)
# 파리의 이동 거리 = ((두 기차 사이의 거리)/(기차의 속도*2))*(파리의 속도)
# 정수형 출력을 위해 int() 사용
print(int(D/(S*2)*T))
