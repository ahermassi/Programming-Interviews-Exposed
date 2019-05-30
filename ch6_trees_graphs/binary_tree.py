from queue import Queue


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
        """
        This is the first depth-first search technique
        node -> left -> right
        :return:
        """

        print(self.data, end=' ')

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        """
        This is the second depth-first search technique
        left -> node -> right
        :return:
        """

        if self.left:
            self.left.in_order()

        print(self.data, end=' ')

        if self.right:
            self.right.in_order()

    def post_order(self):
        """
         This is the third depth-first search technique
        left -> right -> node
        :return:
        """

        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(self.data, end=' ')

    def bfs(self):

        """
        This is the breadth-first search technique
        :return:
        """

        queue = Queue()
        queue.put(self)

        while not queue.empty():

            current_node = queue.get()
            print(current_node.data, end=' ')

            if current_node.left:
                queue.put(current_node.left)

            if current_node.right:
                queue.put(current_node.right)
