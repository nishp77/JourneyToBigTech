from typing import Optional
import sys
from TreeNode import TreeNode


class Solution98:
    def isValidBST(self, root:Optional[TreeNode]):
        return self.valid(root, -sys.maxsize, sys.maxsize)

    def valid(self, root:Optional[TreeNode], left, right):
        if root is None:
            return True
        
        if not (root.val > left and root.val < right):
            return False
        
        return (self.valid(root.left, left, root.val) and self.valid(root.right, root.val, right))