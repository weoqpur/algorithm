import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    pay = int(input())
    five_bill = 50000
    ten_bill = 10000

    print(f"#{tc}")
    for i in range(4):
        print(pay // five_bill, end=" ")
        pay = pay % five_bill
        print(pay // ten_bill, end=" ")
        pay = pay % ten_bill
        five_bill = five_bill // 10
        ten_bill = ten_bill // 10
    print(" ")
