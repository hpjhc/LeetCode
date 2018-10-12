"""
source：https://leetcode.com/problems/roman-to-integer/
author: hpjhc
date: 2018/9/26
"""

class Solution: 
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i, key in enumerate(s):
            nxt = s[i+1:i+2]
            res += dict[key]
            if nxt != '' and dict[key] < dict[nxt]:
                res -= dict[key] * 2
        return res
