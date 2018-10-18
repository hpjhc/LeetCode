"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
author: hpjhc
date: 2018/10/18
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for val in nums[1:]:
            if val != nums[j]:
                j += 1
                nums[j] = val
        return j if not nums else j + 1
