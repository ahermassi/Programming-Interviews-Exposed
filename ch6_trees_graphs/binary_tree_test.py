from binary_tree import BinaryTree

if __name__ == '__main__':

    tree1 = BinaryTree('a')

    print(tree1.data)
    print(tree1.left)
    print(tree1.right)

    tree1.insert_left('b')
    tree1.insert_right('c')

    b_node = tree1.left
    b_node.insert_right('d')

    c_node = tree1.right
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right
    e_node = c_node.left
    f_node = c_node.right

    print(tree1.data)  # a
    print(b_node.data)  # b
    print(c_node.data)  # c
    print(d_node.data)  # d
    print(e_node.data)  # e
    print(f_node.data)  # f

    tree2 = BinaryTree(1)

    tree2.insert_left(2)
    tree2.left.insert_left(3)
    tree2.left.insert_right(4)

    tree2.insert_right(5)
    tree2.right.insert_left(6)
    tree2.right.insert_right(7)

    print("Preorder traversal: ", end='')
    tree2.pre_order()

    print("\nInorder traversal: ", end='')
    tree2.in_order()
