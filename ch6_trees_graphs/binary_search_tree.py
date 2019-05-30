class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):

        if data <= self.data:
            if self.left is None:
                new_node = BinarySearchTree(data)
                self.left = new_node
            else:
                self.left.insert_node(data)

        elif self.right is None:
            new_node = BinarySearchTree(data)
            self.right = new_node
        else:
            self.right.insert_node(data)



