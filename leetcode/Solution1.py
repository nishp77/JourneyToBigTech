from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for i, n in enumerate(nums):
            diff = target - n
            if diff in m:
                return [m[diff], i]
            
            m[n] = i
        


s = Solution1()
s.twoSum([2, 7, 11, 15], 9)
