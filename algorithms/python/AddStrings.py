"""
source：https://leetcode.com/problems/add-strings/
author: hpjhc
date: 2018/9/25
"""

class Solution:
def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    return str(sum((int(num1), int(num2))))
