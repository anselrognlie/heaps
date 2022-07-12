class HeapNode:
  
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class MinHeap:

    def __init__(self):
        self.store = []


    def add(self, key, value = None):
        """ This method adds a HeapNode instance to the heap
            If value == None the new node's value should be set to key
            Time Complexity: O(log n) (height of heap)
            Space Complexity: O(1)
        """
        if value is None:
            value = key

        self.store.append(HeapNode(key, value))
        self.heap_up(len(self.store) - 1)

    def remove(self):
        """ This method removes and returns an element from the heap
            maintaining the heap structure
            Time Complexity: O(log n) (height of heap)
            Space Complexity: O(1)
        """
        if self.empty():
            return None

        self.swap(0, len(self.store) - 1)
        result = self.store.pop()
        self.heap_down(0)
        return result.value

    
    def __str__(self):
        """ This method lets you print the heap, when you're testing your app.
        """
        if len(self.store) == 0:
            return "[]"
        return f"[{', '.join([str(element) for element in self.store])}]"


    def empty(self):
        """ This method returns true if the heap is empty
            Time complexity: O(1)
            Space complexity: O(1)
        """
        return not self.store


    def heap_up(self, index):
        """ This helper method takes an index and
            moves the corresponding element up the heap, if 
            it is less than it's parent node until the Heap
            property is reestablished.
            
            This could be **very** helpful for the add method.
            Time Complexity: O(log n) (height of heap)
            Space Complexity: O(1)
        """
        node = self.store[index]

        while True:
            if index == 0:
                return

            parent = (index - 1) // 2
            parent_node = self.store[parent]
            if parent_node.key <= node.key:
                return

            self.swap(parent, index)

            index = parent

    def heap_down(self, index):
        """ This helper method takes an index and 
            moves the corresponding element down the heap if it's 
            larger than either of its children and continues until
            the heap property is reestablished.
            Time Complexity: O(log n) (height of heap)
            Space Complexity: O(1)
        """

        while index < len(self.store) // 2:
            right = (index + 1) * 2
            has_right = right < len(self.store)
            left = right - 1
            node = self.store[index]
            left_node = self.store[left]
            right_node = self.store[right] if has_right else None

            if (node.key > left_node.key
                or has_right and node.key > right_node.key):
                if has_right and right_node.key < left_node.key:
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
