from node.node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print("List has no items")
            return
        while self.head:
            print(self.head.data, end=' ')
            self.head = self.head.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        while self.head.next:
            self.head = self.head.next
        self.head.next = new_node

    def insert_after_item(self, x, data):
        new_node = Node(data)
        while self.head.data != x and self.head:
            self.head = self.head.next
        if self.head is None:
            print("Item doesn't exist")
            return
        after_node = self.head.next
        self.head.next = new_node
        new_node.next = after_node

    def insert_before_item(self, x, data):
        if self.head is None:
            print("List has no element")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        while self.head.next:
            if self.head.next.data == x:
                break
            self.head = self.head.next
        if self.head.next is None:
            print("Item doesn't exist")
            return
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        if index > 1:
            i = 1
            while i < index - 1 and self.head:
                i = i + 1
                self.head = self.head.next

            if self.head is None:
                print("Index out of bound")
                return
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next = new_node

    def get_count(self):
        if self.head is None:
            return 0
        count = 0
        while self.head:
            count = count + 1
            self.head = self.head.next
        return count

    def search_item(self, x):
        if self.head is None:
            print("List is empty.")
            return
        while self.head:
            if self.head.data == x:
                print("Item found.")
                return True
            self.head = self.head.next
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
        if self.head is None:
            print("List already empty.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List already empty.")
            return
        while self.head.next.next:
            self.head = self.head.next
        self.head.next = None

    def delete_element_by_value(self, x):
        if self.head is None:
            print("No item to delete")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        while self.head.next:
            if self.head.next.data == x:
                break
            self.head = self.head.next
        if self.head.next is None:
            print("Item not found.")
            return
        self.head.next = self.head.next.next


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

    print("\nCount of items: ", linked_list.get_count())

    linked_list.search_item(5)

    linked_list.delete_element_by_value(20)

    linked_list.traverse_list()

    print("Count of items: ", linked_list.get_count())
