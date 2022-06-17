from typing import List


class Solution:
    def findGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[-1])
        i = len(nums) - 2
        while i != -1:
            if nums[i] > max(result):
                result.insert(0, nums[i])
            i -= 1

        return result
            
c = Solution()
c.findGreaterElements([2, 7, 3, 5, 4, 6, 8])

