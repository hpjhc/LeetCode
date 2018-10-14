"""
source：https://leetcode.com/problems/1-bit-and-2-bit-characters/
author: hpjhc
date: 2018/9/21
"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits.pop()
        res = 0
        while(bits and bits.pop()):
            res += 1
        return res % 2 == 0
