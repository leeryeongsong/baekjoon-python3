# https://www.acmicpc.net/problem/17388

# 세 대학의 참여도 점수를 공백을 기준으로 입력받아 리스트 자료형에 저장한다.
point = list(map(int, input().split()))

# 세 대학의 참여도 점수의 합이 100 이상이면 OK 출력
if sum(point) >= 100:
    print('OK')
# 세 대학의 참여도 점수의 합이 100 미만이고, 최솟값이 첫 번째 대학의 값이라면, 해당 대학 Soongsil 출력
elif min(point) == point[0]: 
    print('Soongsil')
# 세 대학의 참여도 점수의 합이 100 미만이고, 최솟값이 두 번째 대학의 값이라면, 해당 대학 Korea 출력
elif min(point) == point[1]:
    print('Korea')
# 세 대학의 참여도 점수의 합이 100 미만이고, 최솟값이 세 번째 대학의 값이라면, 해당 대학 Hanyang 
elif min(point) == point[2]:
    print('Hanyang')
