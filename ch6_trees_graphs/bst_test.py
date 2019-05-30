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

    print(bst.find_node(15))  # True
    print(bst.find_node(10))  # True
    print(bst.find_node(8))  # True
    print(bst.find_node(12))  # True
    print(bst.find_node(20))  # True
    print(bst.find_node(17))  # True
    print(bst.find_node(25))  # True
    print(bst.find_node(19))  # True

    print(bst.find_node(0))  # False

