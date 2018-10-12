"""
source：https://leetcode.com/problems/reverse-integer/
author: hpjhc
date: 2018/10/10
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        flag = False
        if str_x[0] == '-':
           flag = True
           str_x = str_x[1:] 
        str_x = str_x[::-1]
        if flag:
           str_x = '-' + str_x 
        x = int(str_x)
        if x < -2**31 or x > 2**31-1:
                x = 0
        return x
