package leetcode;

import java.util.LinkedList;
import java.util.Queue;

class Solution104 {
    public int maxDepth(TreeNode root) {
        // DFS recursive

        // if (root == null) {
        // return 0;
        // }

        // return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));

        // BFS

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int d = 0;
        while (!queue.isEmpty()) {
            int s = queue.size();
            for (int i = 0; i < s; i++) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    queue.add(node.left);
                }
                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            d++;
        }

        return d;

    }
}