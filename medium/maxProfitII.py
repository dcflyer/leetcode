# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

@author: weichen
"""

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices: return 0
        
        profit = 0
        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff

        return profit
        
if __name__ == "__main__":
    test = Solution() 
    l = [2,1,2,0,1]
    print test.maxProfit(l)           