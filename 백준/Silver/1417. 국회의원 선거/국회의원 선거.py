n = int(input())
vote = []
cnt = 0

for _ in range(n):
    vote.append(int(input()))

first = vote[0]

if n == 1:
    print(0)
else:
    most = max(vote[1:])
    while first <= most:
        vote[vote[1:].index(most) + 1] -= 1
        first += 1
        most = max(vote[1:])
        cnt += 1
    print(cnt)
