from heapq import heapify, heappop, heappush
from typing import List


class Solution1046:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)

            # no max heap in python so we made every value to be negative
            if second > first:
                heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
