import heapq
import time
from sortedcontainers import SortedSet
from collections import defaultdict


# Min-Heap Implementation
class NumberContainersHeap:
    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = defaultdict(list)  # Maps number -> min-heap of indices

    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            return -1

        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]
            if self.index_to_number.get(index) == number:
                return index
            heapq.heappop(self.number_to_indices[number])  # Lazy removal

        return -1


# SortedSet Implementation
class NumberContainersSortedSet:
    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = defaultdict(
            SortedSet
        )  # Maps number -> sorted set of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].discard(index)
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return next(iter(self.number_to_indices[number]))  # Get smallest index
        return -1


# Performance Test
def run_test(impl, name):
    obj = impl()
    operations = 10**5  # Number of operations
    numbers = 1000  # Unique numbers

    # Insert many elements
    start_time = time.time()
    for i in range(operations):
        obj.change(i, i % numbers)  # Assign indices to random numbers

    # Find the minimum index for each number
    for i in range(numbers):
        obj.find(i)

    end_time = time.time()
    print(f"{name} execution time: {end_time - start_time:.4f} seconds")


# Run tests
run_test(NumberContainersHeap, "Min-Heap (heapq)")
run_test(NumberContainersSortedSet, "SortedSet (sortedcontainers)")
