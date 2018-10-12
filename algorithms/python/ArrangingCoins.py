
"""
source：https://leetcode.com/problems/arranging-coins/
author: hpjhc
date: 2018/9/26
"""

class Solution:
def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    from math import sqrt
    if n == 0 or n == 1:
        return n
    else:
        res = int(sqrt(n*2)) - 1
        while (res**2+res)//2 < n:
              res += 1 
        if (res**2+res)//2 == n:
            return res        
        else:
            return res - 1
