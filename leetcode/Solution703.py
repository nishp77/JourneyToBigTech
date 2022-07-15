import heapq
from typing import List


class Solution703:
    def __init__(self, k:int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

s = Solution703(3, [4, 5, 8, 2])
s.add(3)
s.add(5)
s.add(10)
s.add(9)
s.add(4)

