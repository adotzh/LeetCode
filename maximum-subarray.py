"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        
        for num in nums:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        
        return maxSum
