class Heap:
    def __init__(self, arr=None):
        self.heap = arr if arr else []
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)

    def delete_node(self):
        self.heap = [self.heap[len(self.heap) - 1]] + self.heap[1 : len(self.heap) - 1]

        self.build_max_heap()

    def insertion(self, value):
        self.heap.append(value)
        self.build_max_heap()

    def heapSort(self):
        oui = []
        while len(self.heap) != 1:
            firs = self.heap[0]
            oui.append(firs)
            self.delete_node()

        self.heap.extend(oui[::-1])


arr = [4, 12, 96, 10, 36, 10, 63, 1, 0]
heap = Heap(arr)
print(heap.heap)

# heap.delete_node()
# print(heap.heap)
# heap.delete_node()
# print(heap.heap)
#
# heap.insertion(32)
# print(heap.heap)
#

# heap.heapSort()
#
heap.insertion(5)
heap.insertion(11)
print(heap.heap)
heap.insertion(13)
heap.insertion(9)
print(heap.heap)
