# -*- coding: utf-8 -*-
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

@author: Dennis
"""
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if not gas or not cost or len(gas) != len(cost):
            return -1
        
        diff = [x - y for x, y in zip(gas, cost)]
        start, curr, total = 0, 0, 0
        
        for i in xrange(len(diff)):
            total += diff[i]
            curr += diff[i]
            if curr < 0:
                curr = 0
                start = i + 1
        
        return start if total >= 0 else - 1

if __name__ == "__main__":
    test = Solution()
    print test.canCompleteCircuit([5,4,3,2,1], [1,2,3,4,5])
    
            
        
        
