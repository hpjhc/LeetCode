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
        if not needle:
            return 0
        str_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+str_len] == needle:
                return i       
        return -1
