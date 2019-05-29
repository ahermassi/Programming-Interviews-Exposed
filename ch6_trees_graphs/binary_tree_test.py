from binary_tree import BinaryTree

if __name__ == '__main__':

    tree = BinaryTree('a')

    print(tree.data)
    print(tree.left)
    print(tree.right)

    tree.insert_left('b')
    tree.insert_right('c')

    b_node = tree.left
    b_node.insert_right('d')

    c_node = tree.right
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right
    e_node = c_node.left
    f_node = c_node.right

    print(tree.data)  # a
    print(b_node.data)  # b
    print(c_node.data)  # c
    print(d_node.data)  # d
    print(e_node.data)  # e
    print(f_node.data)  # f
