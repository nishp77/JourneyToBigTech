package leetcode;

/**
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 */
public class Solution2 {

    public static void main(String[] args) {

    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum = 0, carry = 0;

        ListNode dummy = new ListNode(-1);
        ListNode top = dummy;

        while (l1 != null || l2 != null) {
            int x = l1 != null ? l1.val : 0;
            int y = l2 != null ? l2.val : 0;

            sum = carry + x + y;
            carry = sum / 10;

            dummy.next = new ListNode(sum % 10);
            dummy = dummy.next;

            if (l1.next != null) {
                l1 = l1.next;
            }

            if (l2.next != null) {
                l2 = l2.next;
            }
        }

        if(carry > 0){
            dummy.next = new ListNode(carry); 
        }

        return top.next;
    }
}
