"""
source: https://leetcode.com/problems/excel-sheet-column-title/
author: hpjhc
date: 2018/10/19
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {}
        import string
        for i in range(26):
            dict[i] = string.ascii_uppercase[i] 
        res = ''
        while n:
            i = (n - 1) % 26
            res = dict[i] + res
            n = (n - 1) // 26
        return res
