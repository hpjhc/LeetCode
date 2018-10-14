"""
source：https://leetcode.com/problems/add-binary/
author: hpjhc
date: 2018/9/22
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        return format(a + b, 'b')
