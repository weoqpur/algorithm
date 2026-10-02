import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    tree_list = list(input().split())

    tree_dict = dict()

    for i in range(0, len(tree_list), 2):
        if tree_dict.get(tree_list[i]) is None: tree_dict[tree_list[i]] = [tree_list[i+1]]
        else: tree_dict[tree_list[i]].append(tree_list[i+1])

    def preorder(tree, node):
        print(node, end=" ")
        if node not in tree: return

        for child in tree[node]:
            preorder(tree, child)

    def inorder(tree, node):
        children = tree.get(node, [])
        if children: inorder(tree, children[0])
        print(node, end=" ")
        if len(children) == 2:
            inorder(tree, tree[node][1])

    def postorder(tree, node):
        for child in tree.get(node, []):
            postorder(tree, child)
        print(node, end=" ")

    preorder(tree_dict, '1')
    print("")
    inorder(tree_dict, '1')
    print("")
    postorder(tree_dict, '1')