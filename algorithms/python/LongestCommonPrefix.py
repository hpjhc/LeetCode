"""
source: https://leetcode.com/problems/longest-common-prefix/
author: hpjhc
date: 2018/10/13
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        try:
            comm = strs[0]
        except IndexError:
            comm = ''        
        for str in strs:
            for i in range(len(comm)):
                if comm[:i+1] != str[:i+1]:
                    comm = comm[:i]
                    break
        return comm
