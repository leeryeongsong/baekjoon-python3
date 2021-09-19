# https://www.acmicpc.net/problem/11943
# 첫 번째 바구니의 사과의 개수와 오렌지의 개수를 공백을 기준으로 입력받아 저장한다.
first_apple, first_orange = map(int, input().split())
# 두 번째 바구니의 사과의 개수와 오렌지의 개수를 공백을 기준으로 입력받아 저장한다.
second_apple, second_orange = map(int, input().split())

# 첫 번째 바구니에는 사과만, 두 번째 바구니에는 오렌지만 남도록 과일을 이동하려면, 두 번째 바구니의 사과 개수와 첫 번째 바구니의 오렌지 개수의 합만큼 이동해야 한다.
first_apple_second_orange = second_apple + first_orange
# 첫 번째 바구니에는 오렌지만, 두 번째 바구니에는 사과만 남도록 과일을 이동하려면, 첫 번째 바구니의 사과 개수와 두 번째 바구니의 오렌지 개수의 합만큼 이동해야 한다.
first_orange_second_apple = first_apple + second_orange

# 위에서 구한 두 개의 숫자, first_apple_second_orange, first_orange_second_apple의 최솟값을 출력한다.
print(min(first_apple_second_orange, first_orange_second_apple))
