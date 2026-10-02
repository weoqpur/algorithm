import sys
sys.stdin = open("input.txt")
import itertools

T = int(input())
for test_case in range(1, T+1):
    N, honey_pot, V = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def cal_square_sum(num_list):
        if sum(num_list) > V:
            return 0
        return sum(num ** 2 for num in num_list)

    def cal_max_honey(honey_list):
        max_honey = 0
        for select_cnt in range(1, honey_pot + 1):
            comb_list = list(map(cal_square_sum, itertools.combinations(honey_list, select_cnt)))
            max_honey = max(max_honey, max(comb_list))
        return max_honey

    max_sum = 0
    for fst_i in range(N):
        for fst_j in range(N - honey_pot + 1):
            fst_select_honey_list = matrix[fst_i][fst_j:fst_j+honey_pot]
            fst_select_honey_max = cal_max_honey(fst_select_honey_list)

            for snd_i in range(fst_i, N):
                for snd_j in range(N - honey_pot + 1):
                    print(fst_i, fst_j, snd_i, snd_j)
                    if fst_i == snd_i and snd_j < fst_j + honey_pot: continue
                    snd_select_honey_list = matrix[snd_i][snd_j:snd_j+honey_pot]
                    snd_select_honey_max = cal_max_honey(snd_select_honey_list)

                    max_sum = max(max_sum, fst_select_honey_max + snd_select_honey_max)
    print(f"#{test_case} {max_sum}")