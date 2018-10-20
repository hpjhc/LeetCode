"""
source: https://leetcode.com/problems/implement-strstr/
author: hpjhc
date: 2018/10/20
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
