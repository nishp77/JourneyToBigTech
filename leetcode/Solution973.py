from heapq import heapify, heappop
from typing import List


class Solution973:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            d = x**2 + y**2
            minHeap.append([d,x,y])
        
        heapify(minHeap)
        res = []
        while k > 0:
            d,x,y = heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res

s = Solution973()
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
