import sys
sys.stdin = open("input.txt", "r")
import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N개의 식재료가 있으며 식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 만들려 한다.
    # A음식, B음식의 맛의 차이가 최소여야 하며 그 맛은 시너지 점수로 결정
    # 식재료 1과 0이 어떤 순서로 들어가냐에 따라 시너지가 다르다
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    item_list = [i for i in range(N)] # 식재료 종류
    a_food_list = itertools.combinations(item_list, N//2) # 식재료 조합
    b_bood_list = list() # 위 조합과 겹치지 않는 조합

    result = float("inf")

    def sum_synergy(food):
        comb_food = itertools.combinations(food, 2)
        comb_sum = 0
        for start, end in comb_food:
            comb_sum += synergy[start][end] + synergy[end][start]
        return comb_sum

    for food in a_food_list:
        b_food = list()
        for item in item_list:
            if item not in food:
                b_food.append(item)
        result = min(result, abs(sum_synergy(food) - sum_synergy(b_food)))



    print(f"#{test_case} {result}")