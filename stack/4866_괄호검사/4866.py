import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    source = input()

    target = {')': '(', ']': '[', '}': '{'}
    stack = []
    result = 1

    for word in source:
        if word in target.values():
            stack.append(word)
        elif word in target.keys():
            if not stack:
                result = 0
                break
            elif stack[-1] != target[word]:
                result = 0
                break
            stack.pop(-1)
    if stack: result = 0
    print(f"#{test_case} {result}")