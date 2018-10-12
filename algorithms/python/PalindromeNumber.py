"""
source：https://leetcode.com/problems/palindrome-number/
author: hpjhc
date: 2018/10/11
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
