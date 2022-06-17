from typing import List
import sys

#Given an integer array nums, find the contiguous subarray (containing at least one number) which 
# has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

class Solution53:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(i, j):
                    sum += nums[k]
                    
