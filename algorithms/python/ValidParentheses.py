"""
source: https://leetcode.com/problems/valid-parentheses/
author: hpjhc
date: 2018/10/15
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {'{':'}', '[':']', '(':')'}
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            elif not stack or ch != dict[stack.pop()]:
                return False
        if stack:
            return False
        return True
