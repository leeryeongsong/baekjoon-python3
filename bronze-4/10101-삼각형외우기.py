# https://www.acmicpc.net/problem/10101
# 삼각형의 세 각을 한 줄에 하나씩 입력받아 저장한다.
angle_A = int(input())
angle_B = int(input())
angle_C = int(input())

# 삼각형 세 각의 합을 구한다.
angle_sum = angle_A + angle_B + angle_C

# 삼각형 세 각 중, 서로 다른 각의 개수를 구한다.
different_angle_count = len(list(set([angle_A, angle_B, angle_C])))

# 모든 각이 60이면 Equilateral을 출력한다.
if angle_A == 60 and angle_B == 60 and angle_C == 60:
    print('Equilateral')
# 세 각의 합이 180이고, 서로 다른 각의 개수가 2이면 = 두 각이 동일하면, Isosceles을 출력한다.
elif angle_sum == 180 and different_angle_count == 2:
    print('Isosceles')
# 세 각의 합이 180이고, 서로 다른 각의 개수가 3이면 = 세 각이 서로 다르면, Scalene을 출력한다.
elif angle_sum == 180 and different_angle_count == 3:
    print('Scalene')
# 세 각의 합이 180이 아니면, Error를 출력한다.
elif angle_sum != 180:
    print('Error')
