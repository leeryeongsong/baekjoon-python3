# https://www.acmicpc.net/problem/1297
# 대각선, 높이 비율, 너비 비율을 공백을 기준으로 입력받아 저장한다.
diagonal, height_ratio, width_ratio = map(int, input().split())
# 피타고라스 정리와 비례식을 이용하면, 대각선 길이 : 루트(높이 비율^2 + 너비 비율^2) = 높이 : 높이 비율 = 너비 : 너비 비율이므로, 아래와 같이 계산했다.  
height = int(diagonal*height_ratio/(height_ratio**2+width_ratio**2)**(1/2))
width = int(diagonal*width_ratio/(height_ratio**2+width_ratio**2)**(1/2))

# 높이와 너비를 공백 한 칸으로 구분하여 출력한다.
print(height, width)
