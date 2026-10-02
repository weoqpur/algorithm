import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())

    result = [0] * 5

    while num != 1:
        if num % 11 == 0:
            result[4] += 1
            num /= 11
        elif num % 7 == 0:
            result[3] += 1
            num /= 7
        elif num % 5 == 0:
            result[2] += 1
            num /= 5
        elif num % 3 == 0:
            result[1] += 1
            num /= 3
        else:
            result[0] += 1
            num /= 2

    print(f"#{test_case} {' '.join(map(str, result))}")