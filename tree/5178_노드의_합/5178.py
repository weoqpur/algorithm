import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N_cnt, leaf_cnt, result_cnt = map(int, input().split())
    node_list = [0] * (N_cnt + 1)

    # 완전 이진 트리이기에 전체 노드 수 만큼의 리스트를 만든 뒤
    # 리프노드의 인덱스 // 2의 인덱스에 합을 할당하며 모든 노드의 값을 구함
    for _ in range(leaf_cnt):
        idx, num = map(int, input().split())
        node_list[idx] = num

    for i in range(N_cnt, result_cnt-1, -1):
        node_list[i//2] += node_list[i]

    print(f"#{test_case} {node_list[result_cnt]}")