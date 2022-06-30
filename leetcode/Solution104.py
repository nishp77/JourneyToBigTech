from collections import deque
from typing import Optional

from TreeNode import TreeNode

class Solution104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    #   DFS
       
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        
        
        
    #   BFS
        
        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     level += 1

        # return level

        
        # DFS Iterative

        stack = [[root,1]]
        result = 1
        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result


s = Solution104()
s.maxDepth([3,9,20,None,None,15,7])


