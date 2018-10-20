"""
source: https://leetcode.com/problems/search-insert-position/
author: hpjhc
date: 2018/10/21
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            l = 0
            r = len(nums)
            while l < r - 1:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid
                else:
                    r = mid 
            return l if nums[l] > target else l + 1
