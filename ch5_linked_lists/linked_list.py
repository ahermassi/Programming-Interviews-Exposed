from node.node import Node


class LinkedList:

    def __init__(self):
        self.start_node = None

    def traverse_list(self):

        if self.start_node is None:
            print("List has no items")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self, data):

        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.start_node is None:
            self.start_node = new_node
            return

        node = self.start_node
        while node.ref is not None:
            node = node.ref
        node.ref = new_node

    def insert_after_item(self, x, data):

        new_node = Node(data)

        before_node = self.start_node
        while before_node.item != x and before_node is not None:
            before_node = before_node.ref

        if before_node is None:
            print("Item doesn't exist")
            return

        after_node = before_node.ref
        before_node.ref = new_node
        new_node.ref = after_node

    def insert_before_item(self, x, data):

        n = self.start_node

        if n is None:
            print("List has no element")
            return

        if n.item == x:
            new_node = Node(data)
            new_node.ref = n
            self.start_node = new_node

        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("Item doesn't exist")
            return

        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    def insert_at_index(self, index, data):

        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node

        if index > 1:
            n = self.start_node
            i = 1
            while i < index - 1 and n is not None:
                i = i + 1
                n = n.ref

            if n is None:
                print("Index out of bound")
                return

            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def get_count(self):

        if self.start_node is None:
            return 0

        count = 0
        n = self.start_node
        while n is not None:
            count = count + 1
            n = n.ref

        return count

    def search_item(self, x):

        if self.start_node is None:
            print("List is empty.")
            return

        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found.")
                return True
            n = n.ref

        print("Item not found.")
        return False

    def make_new_list(self):

        nums = int(input("How many nodes do you want to create ? "))

        if nums == 0:
            return
        for _ in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_at_end(value)

    def delete_at_start(self):

        if self.start_node is None:
            print("List already empty.")
            return

        self.start_node = self.start_node.ref

    def delete_at_end(self):

        if self.start_node is None:
            print("List already empty.")
            return

        n = self.start_node

        while n.ref.ref is not None:
            n = n.ref

        n.ref = None

    def delete_element_by_value(self, x):

        if self.start_node is None:
            print("No item to delete")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("Item not found.")
            return

        n.ref = n.ref.ref


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.insert_at_end(5)
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(15)

    linked_list.insert_at_start(20)

    linked_list.insert_after_item(10, 17)

    linked_list.insert_before_item(17, 25)

    linked_list.insert_at_index(3, 8)

    linked_list.traverse_list()

    print("Count of items: ", linked_list.get_count())

    linked_list.search_item(5)

    linked_list.delete_element_by_value(20)

    linked_list.traverse_list()

    print("Count of items: ", linked_list.get_count())
