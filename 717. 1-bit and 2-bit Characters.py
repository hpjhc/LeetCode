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
        lens = len(bits)    
        if lens == 1:
            return True
        if bits[0] == 0:
            return isOneBitCharacter(bits[1:])
        elif lens == 2:
            return False
        else:
            return isOneBitCharacter(bits[2:])
