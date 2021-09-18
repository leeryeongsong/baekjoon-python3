# https://www.acmicpc.net/problem/5596

# 민국의 네 과목 시험 점수를, 공백으로 구분하여 한 줄에 입력받아 저장한다.
mingug_score = list(map(int, input().split()))
# 만세의 네 과목 시험 점수를, 공백으로 구분하여 한 줄에 입력받아 저장한다.
manse_score = list(map(int, input().split()))

# 민국과 만세의 시험 점수 합을 구한다.
mingug_score_total = sum(mingug_score)
manse_score_total = sum(manse_score)

# 민국과 만세의 시험 점수 합이 같으면, 민국의 점수를 출력하고, 다르면 더 큰 점수를 출력한다.
if mingug_score_total == manse_score_total:
    print(mingug_score_total)
else:
    print(max(mingug_score_total,manse_score_total))
