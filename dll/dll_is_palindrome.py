from dll_intro import DoublyLinkedList

dll_list = DoublyLinkedList(1)
dll_list.append(2)
dll_list.append(3)
dll_list.append(2)
dll_list.append(1)
dll_list.print_list()


def is_palindrome(dll):
    if dll.length == 0 or dll.length == 1:
        return True

    forward = dll.head
    backward = dll.tail
    iterations = dll.length // 2

    for _ in range(1, iterations + 1):
        if forward.value != backward.value:
            return False
        forward = forward.next
        backward = backward.prev

    return True


print(is_palindrome(dll_list))
