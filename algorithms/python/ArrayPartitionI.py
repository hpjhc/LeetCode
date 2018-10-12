"""
source：https://leetcode.com/problems/array-partition-i/
author: hpjhc
date: 2018/10/9
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        return sum(nums[1::2])
