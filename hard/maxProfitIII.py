# -*- coding: utf-8 -*-
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

@author: weichen
"""
class Solution:
    # @param prices, a list of integer
    # @return an integer

# WRONG!!! fails when diff is [1, 2, -2, 3, 2, -5, 2, 5, -9]
#    def maxProfit(self, prices):
#        if not prices: return 0
#
#        profit = 0
#        profitList = []
#        
#        for i in xrange(1, len(prices)):
#            diff = prices[i] - prices[i-1]
#            if diff >= 0:
#                profit += diff
#            else:
#                profitList.append(profit)
#                profit = 0
#                
#        profitList.append(profit)
#        if len(profitList) <= 2:
#            return sum(profitList)
#        else:
#            profitList.sort()
#            return profitList[-1] + profitList[-2]

    def maxProfit(self, prices):
        if not prices: return 0
            
        left = len(prices)*[0]; right = len(prices)*[0]
        min = prices[0]
        for i in xrange(1, len(prices)):
            left[i] = prices[i] - min if prices[i] - min > left[i-1] else left[i-1]
            min = prices[i] if prices[i] < min else min
        
        max = prices[-1]
        for i in xrange(len(prices)-2, -1, -1):
            right[i] = max - prices[i] if max - prices[i] > right[i+1] else right[i+1]
            max = prices[i] if prices[i] > max else max
        
        profit = 0
        for i in xrange(len(prices)):
            profit = left[i] + right[i] if left[i] + right[i] > profit else profit
        return profit    

# generalized to at most k tranactions        
# 我们维护两种量，一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），
# 另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）。
#        
#        global[i][j]=max(local[i][j],global[i-1][j])
#        local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)


#    def maxProfit(self, prices):
#        return self.maxK(prices, 3)
#    
#    def maxK(self, prices, k):
#        if not prices: return 0
#        n = len(prices)
#        globals = [[0]*(k+1) for x in xrange(n)]
#        locals = [[0]*(k+1) for x in xrange(n)]
#        
#        for i in xrange(1, n):
#            diff = prices[i] - prices[i-1]
#            for j in xrange(1, k+1):
#                locals[i][j] = max(globals[i-1][j-1] + max(diff, 0),locals[i-1][j] + diff)
#                globals[i][j] = max(globals[i-1][j], locals[i][j])
#        return globals[n-1][k]
        
if __name__ == "__main__":
    test = Solution()
    l = [1, 2, -2, 3, 2, -5, 2, 5, -9]
    print test.maxProfit(l)        