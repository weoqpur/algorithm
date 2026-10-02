#1 503
#2 55541
#3 334454
#4 5667473
#5 182189737
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split()))
    queue = deque(input().expandtabs())
    line = N // 4

    for i in range(len(queue)):
        pass
