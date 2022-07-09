from turtle import left, right
from typing import Optional
from TreeNode import TreeNode

class Solution124:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def dfs(root):
            if not root: return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # with split check sum

            result[0] = max(result[0], leftMax + rightMax + root.val)

            return max(leftMax, rightMax) + root.val

        
        dfs(root)
        return result[0]