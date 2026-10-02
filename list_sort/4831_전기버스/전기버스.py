import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    range_per_charge, N, charger = map(int, input().split()) # 변수 받기
    bus_range = list(map(int, input().split()))
    bus_range.append(N)
    charge_cnt = 0
    battery = range_per_charge
    for i in range(N):
        if battery + i < bus_range[0]:
            charge_cnt = 0
            break
        if i == bus_range[0]:
            if bus_range[1] > i + battery:
                charge_cnt += 1
                battery = range_per_charge
            bus_range.pop(0)
        battery -= 1

    print(f'#{test_case} {charge_cnt}')
    # ///////////////////////////////////////////////////////////////////////////////////
