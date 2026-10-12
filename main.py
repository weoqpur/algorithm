def make_m(depth, num):
    global result
    if num == K:
        result += 1
        return
    if depth == N: return

    make_m(depth + 1, num)
    make_m(depth + 1, num + depth)

result = 0
N = 10
K = 7

make_m(1, 0)


print(f'#{result}')
