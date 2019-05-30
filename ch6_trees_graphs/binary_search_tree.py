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

    def find_node(self, data):

        if data < self.data and self.left:  # equivalent to ... and self.left is not None
            return self.left.find_node(data)

        if data > self.data and self.right:
            return self.right.find_node(data)

        return self.data == data

    def remove_node(self, data, parent=None):

        if data < self.data and self.left: # target node is to the left and current node has left child
            return self.left.remove_node(data, self) # self in the next call refers to the parent

        elif data < self.data: # target node is to the left but current node has no left child
            return False

        elif data > self.data and self.right: # target node is to the right and current node has right child
            return self.right.reomve_node(data, self)

        elif data > self.data: # target node is to the right but current node has no right child
            return False

        else: # current node is the node to delete; we've got the node and its parent in hand

            if self.left is None and self.right is None:  # leaf node

                if data < parent.data:  # node is to the left of its parent
                    parent.left = None  # delete the paren't left node
                    self.clear_node()
                else:
                    parent.right = None
                    self.clear_node()

            elif self.left and self.right is None:  # node has only a left child

                if data < parent.data:  # node is to the left of its parent
                    parent.left = self.left
                    self.clear_node()
                else: # node is to the right of its parent
                    parent.right = self.left
                    self.clear_node()

            elif self.right and self.left is None:  # node has only a right child

                if data < parent.data:  # node is to the left of its parent
                    parent.left = self.right
                    self.clear_node()
                else: # node is to the right of its parent
                    parent.right = self.right
                    self.clear_node()

            else:  # node has both a left and a right child

                self.data = self.right.find_minimum_value()
                self.right.remove_node(self.data, self)

            return True

    def clear_node(self):
        self.data = None
        self.left = None
        self.right = None

    def find_minimum_value(self):
        if self.left:
            return self.left.find_minimum_value()
        else:
            return self.data
