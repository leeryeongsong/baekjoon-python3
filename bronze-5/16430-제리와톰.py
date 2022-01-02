# https://www.acmicpc.net/problem/16430

# 제리가 1kg 치즈 중 A/Bkg(1<=A<B<=9, A/B는 1이하)만큼 홈쳐가면 남은 치즈의 무게는 B-A/Bkg이다.
A, B = map(int, input().split())
print(B-A, B)
