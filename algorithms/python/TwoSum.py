"""
source：https://leetcode.com/problems/two-sum/
author: hpjhc
date: 2018/10/9
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a_idx, a_val in enumerate(nums):
            for b_idx, b_val in enumerate(nums[a_idx+1:], a_idx+1):
                if a_val + b_val == target:
                    return [a_idx, b_idx]
