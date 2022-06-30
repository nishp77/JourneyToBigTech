package leetcode;

public class Solution543 {
    int d = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return d - 1;
    }

    public int dfs(TreeNode root){
        if (root == null) {
            return 0;
        }

        int leftH = dfs(root.left);
        int rightH = dfs(root.right);

        d = Math.max(d, 1 + leftH + rightH);

        return 1 + Math.max(leftH, rightH);

    }
}
