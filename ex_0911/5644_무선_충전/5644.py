import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t, A = list(map(int, input().split())) # 유저의 행동 수, 충전기의 수
    N = 2 # 유저의 수
    # 유저가 이동하는 경로
    user_move_list = [list(map(int, input().split())) for _ in range(N)]
    # 충전기 위치, 범위, 충전량 리스트
    BC_list = [list(map(int, input().split())) for _ in range(A)]

    dxy = [[0, 0], [-1, 0], [0, 1], [1, 0], [0, -1]]
    result = 0
    a_xy = [1, 1]
    b_xy = [10, 10]
    user_move_list = list(map(list, zip(*user_move_list)))
    # 사용자 A는 지도 1, 1에서 출발 B는 10, 10 출발
    # 사용자 위치와 충전기의 위치 차가 (x + y) - user 절댓값이 충전기의 범위 이하일때 충전
    # 충전기 범위가 겹치면 결과적 충전량이 더 높은 쪽을 선택해 충전한다.
    # 충전기 범위 내부에 사용자가 동시에 존재시 충전량은 절반이 된다.
    # 사용자는 초기 위치부터 충전이 가능하다
    for i in range(t+1):
        a_p_connect = []
        b_p_connect = []
        for j, bc in enumerate(BC_list):
            if abs(bc[1] - a_xy[0]) + abs(bc[0] - a_xy[1]) <= bc[2]: a_p_connect.append(j)
            if abs(bc[1] - b_xy[0]) + abs(bc[0] - b_xy[1]) <= bc[2]: b_p_connect.append(j)
        # 두 사람이 같은 충전기 범위에 있는지 검사
        # 만약 중복된 충전기(반똥가리)보다 다른 충전기가 더 충전량이 높다면 높은 쪽 연결
        # 하나만
        best = 0
        idx = None
        for a_bc in a_p_connect or [None]:
            for b_bc in b_p_connect or [None]:
                a_pw = BC_list[a_bc][3] if a_bc is not None else 0
                b_pw = BC_list[b_bc][3] if b_bc is not None else 0

                if a_bc is not None and a_bc == b_bc:
                    total = a_pw
                else:
                    total = a_pw + b_pw

                best = max(best, total)
        result += best
        if i != t:
            for j in range(2):
                a_xy[j] += dxy[user_move_list[i][0]][j]
                b_xy[j] += dxy[user_move_list[i][1]][j]

    print(f"#{test_case} {result}")