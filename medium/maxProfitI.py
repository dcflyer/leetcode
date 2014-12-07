# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

@author: weichen
"""
class Solution:
    # @param prices, a list of integer
    # @return an integer

# Solution 1: DP
#    def maxProfit(self, prices):
#        if not prices: return 0
#        
#        min = prices[0]
#        profit = 0
#        for i in prices:
#            if i < min: min = i
#            if profit < i - min:
#                profit = i - min
#        
#        return profit

# Solution 2: diff
    def maxProfit(self, prices):
        if not prices: return 0

        profit = 0
        curr = 0
        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if curr + diff < 0:
                curr = 0
            else:
                curr += diff
                if curr > profit:
                    profit = curr
        return profit
                
        
if __name__ == "__main__":
    test = Solution()
    import numpy as np
    l = list(np.random.randint(0,9,10))
    print l, test.maxProfit(l)