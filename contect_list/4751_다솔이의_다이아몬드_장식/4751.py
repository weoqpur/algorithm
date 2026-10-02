import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    text = input()
    one_line = "..#." * len(text) + "."
    two_line = ".#.#" * len(text) + "."
    middle = ""
    for char in text:
        middle += f"#.{char}."
    middle += "#"

    print(one_line)
    print(two_line)
    print(middle)
    print(two_line)
    print(one_line)