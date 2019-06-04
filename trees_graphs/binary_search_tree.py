class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        """
        This method inserts a new node with value <data> into the BST
        :param data: value of node to insert
        :return:
        """

        if data <= self.data:  # if value to insert is less than or equal the current node's value, then insert to left
            if self.left is None:
                new_node = BinarySearchTree(data)
                self.left = new_node  # the new node is the only left child of the current node
            else:
                self.left.insert_node(data)  # recursive call to current nodes's left subtree

        elif self.right is None:  # if value to insert is greater than the current node's value, then insert to right
            new_node = BinarySearchTree(data)
            self.right = new_node  # the new node is the only right child of the current node
        else:
            self.right.insert_node(data) # recursive call to current nodes's right subtree

    def find_node(self, data):
        """
        This method searches for node of value <data> in the BST.
        :param data: value of sought node
        :return: boolean (value found or not)
        """

        if data < self.data and self.left:  # if sought value is less than current node's value, then look to the left
            return self.left.find_node(data)  # recursive call to current nodes's left subtree

        if data > self.data and self.right:  # if sought value is greater than current node's value, look to the right
            return self.right.find_node(data)  # recursive call to current nodes's right subtree

        return self.data == data  # stationary condition: the entire subtree has been checked. Return value found or not

    def remove_node(self, data, parent=None):
        """
        This method removes a node of value <data> from the BST
        :param data: value of node to remove
        :param parent: parent of node to remove
        :return: boolean (node removed or not)
        """

        if data < self.data and self.left:  # if target node is to the left and current node has left child ...
            return self.left.remove_node(data, self)  # then recursively call remove_node on left subtree with
            # current node as parent

        elif data < self.data:  # if target node is to the left but current node has no left child, removal fails
            return False

        elif data > self.data and self.right: # if target node is to the right and current node has right child ...
            return self.right.remove_node(data, self)  # then recursively call remove_node on right subtree with
            # current node as parent

        elif data > self.data:  # if target node is to the right but current node has no right child, removal fails
            return False

        else:  # current node is the node to delete; we've got the node and its parent in hand

            if self.left is None and self.right is None:  # node to delete is a leaf node

                if data < parent.data:  # node to delete is to the left of its parent
                    parent.left = None  # delete the paren't left node
                    self.clear_node()
                else:
                    parent.right = None
                    self.clear_node()

            elif self.left and self.right is None:  # node to delete has only a left child

                if data < parent.data:  # node to delete is to the left of its parent
                    parent.left = self.left
                    self.clear_node()
                else:  # node to delete is to the right of its parent
                    parent.right = self.left
                    self.clear_node()

            elif self.right and self.left is None:  # node to delete has only a right child

                if data < parent.data:  # node to delete is to the left of its parent
                    parent.left = self.right
                    self.clear_node()
                else: # node to delete is to the right of its parent
                    parent.right = self.right
                    self.clear_node()

            else:  # node to delete has both a left and a right child

                self.data = self.right.find_minimum_value()  # search for the minimum node in the right subtree
                self.right.remove_node(self.data, self)

            return True

    def clear_node(self):
        self.data = None
        self.left = None
        self.right = None

    def find_minimum_value(self):
        if self.left:  # minimum value should be to the left
            return self.left.find_minimum_value()  # recursive call on the left subtree
        else:
            return self.data

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
