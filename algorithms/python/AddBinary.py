"""
source：https://leetcode.com/problems/add-binary/
author: hpjhc
date: 2018/9/22
"""

 class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            temp = a
            a = b
            b = temp    
        lens = len(a)    
        i = 0
        flag = 0
        while i < lens:
            if i < len(b):
                num = int(a[i]) + int(b[i]) + flag    
                if num > 1:
                    res += str(num % 2)
                    flag = num // 2
                else:
                    res += str(num)
                    flag = 0    
            else:
                num = int(a[i]) + flag       
                if num > 1:
                    res += str(num % 2)
                    flag = num // 2
                else:
                    res += str(num)
                    flag = 0
            i += 1
        if flag:
            res += '1'             
        return res[::-1]
