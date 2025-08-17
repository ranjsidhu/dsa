from linked_lists.singly_linked_lists import Node


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        print("------- Printing queue starts -------")
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("------- Printing queue ends -------")

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return new_node

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


queue = Queue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.print_queue()
queue.dequeue()
queue.print_queue()
