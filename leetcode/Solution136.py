#Given a non-empty array of integers nums, every element appears twice except for one. 
# 
# Find that single one.


# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import List


class Solution136:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for n in nums:
            result = n ^ result
        
        return result