package leetcode;

import java.util.*;

public class Solution199 {
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        List<Integer> result = new ArrayList<>();
        if (root != null) {
            q.add(root);
        }

        while (!q.isEmpty()) {
            int s = q.size();
            for (int i = 0; i < s; i++) {
                
                TreeNode node = q.remove();
                
                if (i == s - 1) {
                    result.add(node.val);
                }

                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
            }
        }

        return result;

    }
}
