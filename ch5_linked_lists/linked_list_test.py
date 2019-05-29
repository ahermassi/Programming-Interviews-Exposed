from node.linked_list import LinkedList

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