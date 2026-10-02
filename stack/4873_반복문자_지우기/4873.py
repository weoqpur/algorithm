import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    source = input()
    tmp = source

    for char in source:
        if char+char in tmp:
            idx = tmp.find(char+char)
            tmp = tmp[:idx]+tmp[idx+2:]

    print(f"#{test_case} {len(tmp)}")



