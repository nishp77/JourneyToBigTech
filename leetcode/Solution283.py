from typing import List

class Solution283:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        result = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result

s = Solution283()
s.productExceptSelf([1,2,3,4])
