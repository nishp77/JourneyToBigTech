package leetcode;

public class Solution572 {
    public boolean isSubTree(TreeNode root, TreeNode subroot) {
       
        if(subroot == null) {
            return true;
        }
        if (root == null) {
            return false;
        }

        if(isSameTree(root, subroot)){
            return true;
        }

        return isSubTree(root.left, subroot) || isSubTree(root.right, subroot);
    }

    public boolean isSameTree(TreeNode root, TreeNode subroot) {
        if (root == null && subroot == null) {
            return true;
        }

        if(root == null || subroot == null || root.val != subroot.val){
            return false;
        }

        return isSameTree(root.left, subroot.left) && isSameTree(root.right, subroot.right);
    }
}
