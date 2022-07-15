from TreeNode import TreeNode


class Solution297:
    def serialize(self,root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
    
    def deserialize(self,data):
        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "N":
                self.i += 1
                return None
            
            n = TreeNode(int(val[self.i]))
            self.i += 1
            n.left = dfs()
            n.right = dfs()

            return n
        
        return dfs()
