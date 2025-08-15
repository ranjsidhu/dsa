class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        print("------- Printing list starts -------")
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("------- Printing list ends -------")

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if self.length == 0 or index > self.length - 1:
            return None
        temp = self.head
        if index == 0 and temp is not None:
            return temp.value
        count = 0
        while count != index:
            temp = temp.next
            count += 1

        return temp

    def get_by_binary_search(self, index):
        if self.length == 0 or index > self.length - 1:
            return None

        if index < self.length / 2:
            return self.get(index)
        else:
            temp = self.tail
            steps = self.length - 1 - index
            for _ in range(steps):
                temp = temp.prev

            return temp

    def set_value(self, index, value):
        node = self.get_by_binary_search(index)
        if node:
            node.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get_by_binary_search(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True


dll = DoublyLinkedList(1)
