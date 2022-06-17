package leetcode;

/**
 * Given an integer x, return true if x is palindrome integer.
 * 
 * An integer is a palindrome when it reads the same backward as forward.
 * 
 * For example, 121 is a palindrome while 123 is not.
 */

public class Solution9 {

    public static void main(String[] args) {
        System.out.println(isPalindrome(-121));
    }

    public static boolean isPalindrome(int x) {

        // Not the best way to solve it

        // String temp = x + "";
        // int right;
        // int left = temp.length() / 2 - 1;

        // if (temp.length() % 2 == 0) {
        // right = temp.length() / 2;
        // } else {
        // right = temp.length() / 2 + 1;
        // }

        // while (left > -1 && right < temp.length()) {
        // if(temp.charAt(left--) != temp.charAt(right++)) return false;
        // }

        // return true;

        // We can use mathematics to solve it

        if(x<0) return false;

        int n = x;
        int r = 0;
        while (n != 0) {
            r = n % 10 + r * 10;
            n = n / 10;
        }

        return x == r;
    }
}
