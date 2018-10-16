"""
source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
author: hpjhc
date: 2018/10/16
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = prices[0]
        sell = 0
        res = 0
        for val in prices[1:]:
            if val < buy:
                if sell > buy:
                    res += sell - buy
                buy = val
                sell = 0
            elif val > sell:
                sell = val
            elif val == sell:
                res += val - buy
                buy = val
                sell = 0
            else:
                res += sell - buy
                buy = val
                sell = 0
        if sell > buy:
            res += sell - buy
        return res
