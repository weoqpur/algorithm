import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text = input()
    target = {'b':'d', 'q':'p', 'd':'b', 'p':'q'}
    result = ""
    for char in text:
        result += target[char]

    print(f"#{test_case} {result[::-1]}")