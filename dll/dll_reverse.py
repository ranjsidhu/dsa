from dll_intro import DoublyLinkedList

dll_list = DoublyLinkedList(1)
dll_list.append(2)
dll_list.append(3)
dll_list.append(4)
dll_list.append(5)
dll_list.print_list()


def reverse_dll(dll: DoublyLinkedList):
    current = dll.head
    temp = None

    while current:
        next_node = current.next
        current.next = temp
        current.prev = next_node

        temp = current
        current = next_node

    dll.tail = dll.head
    dll.head = temp


reverse_dll(dll_list)
dll_list.print_list()
