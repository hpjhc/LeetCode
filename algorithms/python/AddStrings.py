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
        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2:
            lens = len2
            num1 = '0'*(lens-len1)+num1
        else:
            lens = len1   
            num2 = '0'*(lens-len2)+num2
        i =  lens - 1   
        flag = 0
        res = ""
        while i >= 0:
            temp = int(num1[i]) + int(num2[i]) + flag
            res = str(temp % 10) + res
            if temp >= 10:
                flag = 1
            else:
                flag = 0 
            i -= 1  
        if flag:
            res = '1' + res  
        return res
