from collections import deque
from typing import List, Optional
from TreeNode import TreeNode

class Solution102:
    def levelOrder(self, root:Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root: queue.append(root)
        result = []

        while queue:
            val = []

            for i in range(len(queue)):
                node = queue.popleft()
                val.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            result.append(val)
        
        return result
