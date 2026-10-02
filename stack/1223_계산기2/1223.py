import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    N = int(input())
    text = input()
    opr_dict = {'*':2, '+':1, '#':0}

    opr_list = []
    result = []
    # 1. 피연산자시 피연산자 스택에 push
    # 2. 연산자시 연산자 스택에 push 그러나 여기서 내부에 이미 연산자가 있다면 우선순위 비교
    # 2-1. 우선순위가 같거나 더 크다면 스택의 모든 연산자를 pop 더 작다면 그냥 append
    for i in text.strip() + '#':
        if i.isnumeric():
            result.append(i)
            continue
        elif not opr_list:
            opr_list.append(i)
            continue
        elif opr_dict.get(i) >= opr_dict.get(opr_list[-1]):
            opr_list.append(i)
            continue
        for _ in range(len(opr_list)):
            op1 = int(result.pop())
            op2 = int(result.pop())
            opr = opr_list.pop()
            if opr == '*': result.append(op1 * op2)
            else: result.append(op1 + op2)
        if i != '#':
            opr_list.append(i)
    print(f"{test_case} {result[0]}")
