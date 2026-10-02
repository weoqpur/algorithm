import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    word_list = [input().strip() for _ in range(N)]

    def sub_comb(n, word_comb):
        if n == N:
            return int(len(word_comb) == 26)
        skip = sub_comb(n+1, word_comb)
        pick = sub_comb(n+1, word_comb | set(word_list[n]))

        return skip + pick

    result = sub_comb(0, set())
    print(f"#{tc} {result}")
