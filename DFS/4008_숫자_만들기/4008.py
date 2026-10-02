import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    op_input_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    min_num = float("inf")
    max_num = float("-inf")

    # 1. 종료 조건 ( depth => depth 위치에 어떤 연산자를 고려할지)
    # 2. 누적해서 가져가고 싶은 값 (선택한 연산자를 기반으로 계산한 결과)
    def dfs(n, num_sum, op_list):
        global min_num, max_num
        if n == N:
            min_num = min(min_num, num_sum)
            max_num = max(max_num, num_sum)
            return

        for idx, op_cnt in enumerate(op_list):
            if op_cnt == 0: continue

            tmp = num_sum
            if idx == 0:
                tmp += num_list[n]
            elif idx == 1:
                tmp -= num_list[n]
            elif idx == 2:
                tmp *= num_list[n]
            elif idx == 3:
                if num_list[n] == 0: return
                tmp = int(tmp / num_list[n])

            op_list[idx] -= 1
            dfs(n+1, tmp, op_list)
            op_list[idx] += 1

    dfs(1, num_list[0], op_input_list)
    print(f"#{tc} {max_num - min_num}")