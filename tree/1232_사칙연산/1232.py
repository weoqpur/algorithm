import sys
sys.stdin = open("input.txt", "r")
from collections import defaultdict

T = 10
for tc in range(1, T + 1):
    N = int(input())
    node_dict = defaultdict(list)
    for _ in range(N):
        tmp = input().strip().split()
        node_dict[int(tmp[0])] = tmp[1:]

    def tree(node):
        node_v = node_dict[node]
        if len(node_v) != 1:
            ob1 = tree(int(node_v[1]))
            ob2 = tree(int(node_v[2]))
            opr = node_v[0]
            if opr == '+': return ob1 + ob2
            elif opr == '-': return ob1 - ob2
            elif opr == '*': return ob1 * ob2
            elif opr == '/': return ob1 / ob2
        else: return int(node_v[0])

    print(f"#{tc} {int(tree(1))}")
