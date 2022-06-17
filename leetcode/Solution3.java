package leetcode;

import java.util.HashMap;

/**
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 */
public class Solution3 {
    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("pwwkew"));
    }

    public static int lengthOfLongestSubstring(String s) {
        int i =0;

        HashMap<Character,Integer> map = new HashMap<>();
        while(i<s.length()){
            while(map.containsKey(s.charAt(i))){
                map.remove(s.charAt(i));
            }
            map.put(s.charAt(i), i);
            i++;
        }

        return map.size();
    }
}
