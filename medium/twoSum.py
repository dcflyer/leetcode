# -*- coding: utf-8 -*-
"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 

@author: n609874
"""
class Solution: 
    # @return a tuple, (index1, index2) 
#    def twoSum(self, num, target):
#        processed = {}
#        for i in xrange(len(num)):
#            if target - num[i] in processed:
#                return processed[target - num[i]] + 1, i + 1
#            else:
#                processed[num[i]] = i

    def twoSum(self, num, target):
        processed = {}
        for i, j in enumerate(num):
            if target - j in processed:
                return processed[target - j] + 1, i + 1
            else:
                processed[j] = i


if __name__ == "__main__":
    test = Solution()
    A = [2,4,5,1]
    print A
    print test.twoSum(A, 3)
