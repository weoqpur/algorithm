import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    price_list = [int(input()) for _ in range(N)]
    weight_list = [int(input()) for _ in range(M)]
    parking_list = [0] * N
    wait_list = []
    result = 0

    # 차량이 들어오면 주차여부를 판단하는 리스트를 False로
    # 바꾸고 차량의 무게와 그 칸의 요금을 곱한 뒤 result에 추가
    for _ in range(M*2):
        car_idx = int(input())
        if car_idx > 0:
            for i in range(N):
                if parking_list[i] == 0:
                    parking_list[i] += car_idx
                    result += price_list[i] * weight_list[car_idx-1]
                    break
            else:
                wait_list.append(car_idx)
        else:
            for i in range(N):
                if (parking_list[i] + car_idx) == 0:
                    parking_list[i] += car_idx
                    if wait_list:
                        parking_list[i] += wait_list.pop(0)
                        result += price_list[i] * weight_list[parking_list[i]-1]
                    break

    print(f"#{test_case} {result}")




