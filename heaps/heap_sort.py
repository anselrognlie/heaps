# from .min_heap import MinHeap

# def heap_sort(list):
#     """ This method uses a heap to sort an array.
#             Time Complexity: O(n log n) (number of els * height of heap)
#             Space Complexity: O(n) (copy of data)
#     """
#     heap = MinHeap()
#     for val in list:
#         heap.add(val)

#     result = []
#     while not heap.empty():
#         result.append(heap.remove())

#     return result

from .in_place_max_heap import InPlaceMaxHeap

def heap_sort(list):
    """ This method uses a heap to sort an array.
            Time Complexity: O(n log n) (number of els * height of heap)
            Space Complexity: O(1) (in-place)
    """
    heap = InPlaceMaxHeap(list)
    heap.make_heap()
    heap.unmake_heap()

    return list
