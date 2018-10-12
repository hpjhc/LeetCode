"""
source: https://leetcode.com/problems/assign-cookies/
author: hpjhc
date: 2018/10/13
"""

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i = 0
        res = 0
        for val in g:
            while i < len(s) and val > s[i]:
                i += 1
            if i < len(s):
                res += 1    
                i += 1          
        return res

