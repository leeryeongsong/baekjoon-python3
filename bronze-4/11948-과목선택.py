# https://www.acmicpc.net/problem/11948

# 6과목 성적을 입력받을 score 변수를 빈 리스트로 선언한다.
score = []

# for문으로 6과목 성적을 한 줄에 하나씩 입력받아 score 리스트에 추가한다.
for i in range(6):
    score.append(int(input()))

# 첫 번째 과목부터 네 번째 과목 중, 큰 값으로 3과목을 선택해서 합을 구해야 하는데, 이는 score 인덱스 0부터 3까지의 합을 구하고, 인덱스 0부터 3까지 값 중 최소값만큼 빼면 된다.
# 다섯 번째 과목과 여섯 번째 과목 중 더 큰 값으로 선택해서 score_sum에 더한다.
score_sum = sum(score[:4]) - min(score[:4]) + max(score[4], score[5])
# score_sum을 출력한다.
print(score_sum)
