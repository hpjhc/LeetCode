
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
    l = 0
    r = n
    while l < r:
        mid = (l + r) // 2
        res = n - mid * (mid + 1) // 2
        if res > mid:
            l = mid + 1          
        else:
            r = mid
    return l
