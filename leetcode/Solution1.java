package leetcode;

import java.util.HashMap;

/**
 * Solution1
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 * 
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 * 
 * You can return the answer in any order.
 */
public class Solution1 {

    public static void main(String[] args) {

    }

    public int[] twoSum(int[] nums, int target) {
        // worst case n^2

        // for (int i = 0; i < nums.length; i++) {
        // for (int j = i+1; j < nums.length; j++) {
        // if(nums[i] + nums[j] == target) {
        // return new int[] {i, j};
        // }
        // }
        // }

        
        // time complexity = O(n)
        // space complexity = O(n)

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[] { map.get(target - nums[i]), i };
            }
            map.put(nums[i], i);
        }

        return new int[] {};
    }
}