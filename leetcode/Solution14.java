package leetcode;

public class Solution14 {
    public static void main(String[] args) {
        System.out.println(longestCommonPrefix(new String[] { "fli", "flower", "flow", "flight" }));
    }

    public static String longestCommonPrefix(String[] strs) {

        if (strs.length == 0)
            return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
            }
        }
        return prefix;
    }

}
