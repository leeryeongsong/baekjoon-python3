# https://www.acmicpc.net/problem/20499
# /를 기준으로 나누어 입력받고, int형으로 변환하여 K, D, A에 각각 저장한다.
K, D, A = map(int, input().split('/'))
# K+A < 0 이거나, D == 0이면 hasu를 출력한다.
if K + A < D or D == 0 :
    print('hasu')
# 위 사례에 해당하지 않으면 gosu를 출력한다.
else:
    print('gosu')
