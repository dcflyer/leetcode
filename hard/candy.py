# -*- coding: utf-8 -*-
"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

@author: Dennis
"""

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings: return 0
        
        num = [1]*len(ratings)
        
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                num[i] = num[i - 1] + 1
        
        res = num[len(ratings) - 1]
        
        for i in xrange(len(ratings) - 2, -1, -1):
            curr = 1
            if ratings[i] > ratings[i + 1]:
                curr = num[i + 1] + 1
            res += max(curr, num[i])
            num[i] = curr
        
        return res

if __name__ == '__main__':
    test = Solution()
    print test.candy([3,2,1,2,1,3,2,4])
        
        