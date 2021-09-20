# https://www.acmicpc.net/problem/15963
# 필요한 배터리 번호와 지금 받을 수 있는 배터리 번호를 공백을 기준으로 입력받아 저장한다.
need, exist = map(int, input().split())
# 필요한 배터리 번호와 지금 받을 수 있는 배터리 번호가 동일하면 1출력, 동일하지 않다면 0을 출력한다.
if need == exist:
    print(1)
else:
    print(0)
