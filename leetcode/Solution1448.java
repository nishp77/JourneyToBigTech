package leetcode;

public class Solution1448 {
    int n = 0;
    public int goodNodes(TreeNode root) {
        dfs(root, Integer.MIN_VALUE);
        return n;
    }

    public void dfs(TreeNode root, int max) {
        if (root == null) {
            return ;
        }

        if(root.val >= max){
            n++;
        }

        if(root.left!=null){
            dfs(root.left, Math.max(max, root.val));
        }
        
        if (root.right != null) {
            dfs(root.right, Math.max(max, root.val));
        }

    }
}
