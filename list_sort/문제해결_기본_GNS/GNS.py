import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num, N = input().split()
    num_str = list(input().split())
    vocab = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    numbers = [0] * 10
    for num in num_str:
        numbers[vocab.index(num)] += 1

    result = ""
    for str_num, num in zip(vocab, numbers):
        result += f'{str_num} ' * num

    print(f'#{test_case}')
    print(result)