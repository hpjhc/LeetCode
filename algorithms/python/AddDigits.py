"""
source：https://leetcode.com/problems/add-digits/
author: hpjhc
date: 2018/9/23
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            a = num % 10
            b = num // 10
            num = a + b
        return num    
        
