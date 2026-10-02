import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input()) # N 개까지 369를 이어가야 함
    result = '1'
    for i in range(2, N+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            num_3 = str(i).count('3')
            num_6 = str(i).count('6')
            num_9 = str(i).count('9')
            result += f' {"-"*(num_3+num_6+num_9)}'
        else:
            result += f' {i}'
    print(result)

    # ///////////////////////////////////////////////////////////////////////////////////
