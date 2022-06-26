from typing import List

class Solution42:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        l,r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        result = 0
        
        while l<r:
            if leftMax < rightMax:
                leftMax += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                rightMax -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]

        return result
