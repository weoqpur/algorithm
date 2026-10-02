import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    dump_epoch = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(dump_epoch):
        max_idx, min_idx = boxes.index(max(boxes)), boxes.index(min(boxes))
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    result = max(boxes) - min(boxes)
    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
