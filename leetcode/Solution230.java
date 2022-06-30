package leetcode;

import java.util.Stack;

public class Solution230 {
    public int kthSmallest(TreeNode node, int k) {
        Stack<TreeNode> s = new Stack<>();
        int n = 0;
        TreeNode curr = node;

        while(curr!= null|| s.size()>0){
            while(curr!=null) {
                s.push(curr);
                curr = curr.left;
            }

            curr = s.pop();
            n++;
            if(n==k){
                return curr.val;
            }
            curr = curr.right;
        }


    }
}
