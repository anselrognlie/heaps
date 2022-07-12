class InPlaceMaxHeap:

    def __init__(self, buffer, key=None, value=None):
        self.store = buffer
        self.key = InPlaceMaxHeap.get_key_direct if key is None else key
        self.value = InPlaceMaxHeap.get_value_direct if value is None else value

    @staticmethod
    def get_key_direct(node):
        return node

    @staticmethod
    def get_value_direct(node):
        return node

    def make_heap(self):
        start = 0
        end = 1

        while end < len(self.store):
            end += 1
            insert = end - 1
            self.heap_up(insert)

    def heap_up(self, index):
        node = self.store[index]

        while True:
            if index == 0:
                return

            parent = (index - 1) // 2
            parent_node = self.store[parent]
            if self.key(parent_node) >= self.key(node):
                return

            self.swap(parent, index)

            index = parent

    def unmake_heap(self):
        start = 0
        end = len(self.store)

        while end > 0:
            end -= 1
            self.swap(0, end)
            self.heap_down(0, end)

    def heap_down(self, index, end):
        while index < end // 2:
            right = (index + 1) * 2
            has_right = right < end
            left = right - 1
            node = self.store[index]
            left_node = self.store[left]
            right_node = self.store[right] if has_right else None

            if (self.key(node) < self.key(left_node)
                or has_right and self.key(node) < self.key(right_node)):
                if has_right and self.key(right_node) > self.key(left_node):
                    swap = right
                else:
                    swap = left

                self.swap(index, swap)
                index = swap
            else:
                return
    
    def swap(self, index_1, index_2):
        """ Swaps two elements in self.store
            at index_1 and index_2
            used for heap_up & heap_down
        """
        temp = self.store[index_1]
        self.store[index_1] = self.store[index_2]
        self.store[index_2] = temp
