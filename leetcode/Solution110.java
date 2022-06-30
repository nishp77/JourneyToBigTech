package leetcode;

public class Solution110 {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        
        }

        return Math.abs(height(root.left) - height(root.right)) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }

    private int height(TreeNode hNode){
        if (hNode == null){
            return 0;
        }

        return 1 + Math.max(height(hNode.left), height(hNode.right));
    }
}
