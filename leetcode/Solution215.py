from heapq import _heapify_max, heapify, heappop
from typing import List


class Solution215:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        
        return nums[0]

s = Solution215()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))