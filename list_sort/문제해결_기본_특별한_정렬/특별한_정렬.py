import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 1. 목표가 제일 큰 수 5개 제일 작은 수 5개를 찾으면 되기에 min max 전략으로 접근
    # 2. 순회하면서 min max 값 탐지 후 list에서 pop 시키고 결과 리스트에 저장
    # 3. 5번 반복
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    numbers = list(map(int, input().split()))
    result = ""

    for _ in range(5):
        min_value = numbers[0]
        max_value = numbers[0]
        for num in numbers:
            if min_value > num:
                min_value = num
            if max_value < num:
                max_value = num
        max_idx = numbers.index(max_value)
        result += f'{str(numbers.pop(max_idx))} '
        min_idx = numbers.index(min_value)
        result += f'{str(numbers.pop(min_idx))} '

    print(f'#{test_case} {result}')