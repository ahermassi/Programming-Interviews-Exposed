from binary_search_tree import BinarySearchTree

if __name__ == '__main__':

    bst = BinarySearchTree(15)

    bst.insert_node(10)
    bst.insert_node(8)
    bst.insert_node(12)
    bst.insert_node(20)
    bst.insert_node(17)
    bst.insert_node(25)
    bst.insert_node(19)

    #       | 15 |
    #      /      \
    #    |10|     |20|
    #   /    \    /    \
    # |8|   |12| |17| |25|
    #              \
    #              |19|

    print(bst.find_node(15))  # True
    print(bst.find_node(10))  # True
    print(bst.find_node(8))  # True
    print(bst.find_node(12))  # True
    print(bst.find_node(20))  # True
    print(bst.find_node(17))  # True
    print(bst.find_node(25))  # True
    print(bst.find_node(19))  # True

    print(bst.find_node(0))  # False

    print(bst.pre_order())

    bst.remove_node(8)

    #     |15|
    #   /      \
    # |10|     |20|
    #    \    /    \
    #   |12| |17| |25|
    #          \
    #          |19|

    print(bst.pre_order())

    bst.remove_node(17)

    #        |15|
    #      /      \
    #    |10|     |20|
    #       \    /    \
    #      |12| |19| |25|

    print(bst.pre_order())

    bst.remove_node(15)

    #        |19|
    #      /      \
    #    |10|     |20|
    #        \        \
    #        |12|     |25|

    print(bst.pre_order())


