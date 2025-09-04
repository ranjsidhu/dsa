class MaxHeap:
    def __init__(self):
        self.heap = []

    def print_heap(self):
        print(self.heap)

    def _left_child(self, index: int):
        return 2 * index + 1

    def _right_child(self, index: int):
        return 2 * index + 2

    def _parent(self, index: int):
        return (index - 1) // 2

    def _swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = (
            self.heap[index2],
            self.heap[index1],
        )

    def _sink_down(self, index: int = None):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (
                left_index < len(self.heap)
                and self.heap[left_index] > self.heap[max_index]
            ):
                max_index = left_index

            if (
                right_index < len(self.heap)
                and self.heap[right_index] > self.heap[max_index]
            ):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value: int):
        """
        Adds to the bottom of the heap so the heap is complete
        Promotes the value to the appropriate indexes
        """
        self.heap.append(value)
        current = len(self.heap) - 1

        while (
            current > 0
            and self.heap[current] > self.heap[self._parent(current)]  # noqa
        ):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        """
        Removes the root node
        Demotes nodes to the appropriate indexes
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


heap = MaxHeap()

heap.insert(95)
heap.insert(75)
heap.insert(80)
heap.insert(55)
heap.insert(60)
heap.insert(50)
heap.insert(65)
heap.print_heap()

heap.remove()
heap.print_heap()

heap.remove()
heap.print_heap()
