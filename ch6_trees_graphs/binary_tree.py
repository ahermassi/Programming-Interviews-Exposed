class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_left(self, data):

        if self.left is None:
            self.left = BinaryTree(data)

        else:
            new_node = BinaryTree(data)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, data):

        if self.right is None:
            self.right = BinaryTree(data)

        else:
            new_node = BinaryTree(data)
            new_node.right = self.right
            self.right = new_node

    def pre_order(self):
        '''
        This is the first depth-first search technique
        node -> left -> right
        :return:
        '''

        print(self.data)

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    