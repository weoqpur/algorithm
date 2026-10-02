import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, kcal_limit = map(int, input().split())
    food_list = []
    max_score = 0
    result_kcal = 0

    for _ in range(N):
        food_list.append(list(map(int, input().split())))

    def sub_comb(n, score, kcal):
        global max_score
        if kcal <= kcal_limit and score > max_score: max_score = score
        if n == N or kcal > kcal_limit: return

        sub_comb(n+1, score+food_list[n][0], kcal+food_list[n][1])
        sub_comb(n+1, score, kcal)

    sub_comb(0, max_score, result_kcal)

    print(f"#{tc} {max_score}")