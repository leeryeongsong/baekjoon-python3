# https://www.acmicpc.net/problem/3003
import sys

correct = [1, 1, 2, 2, 2, 8]
white_piece = list(map(int, sys.stdin.readline().split()))

for i in range(6):
    white_piece[i] = correct[i] - white_piece[i]
    print(white_piece[i], end=' ')
